import os
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)
import frontmatter
import glob
import logging
from datetime import datetime, timedelta
from pathlib import Path

# ロガーの設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def get_ga4_metrics(property_id, credentials_path):
    logger.info(f"GA4メトリクスの取得を開始します（property_id: {property_id}）")
    try:
        client = BetaAnalyticsDataClient.from_service_account_json(credentials_path)
        
        # 過去90日間のデータを取得
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=90)
        logger.info(f"期間: {start_date} から {end_date}")
        
        request = RunReportRequest(
            property=f"properties/{property_id}",
            dimensions=[
                Dimension(name="pagePath"),
            ],
            metrics=[
                Metric(name="screenPageViews"),
                Metric(name="totalUsers"),
                Metric(name="averageSessionDuration"),
            ],
            date_ranges=[
                DateRange(
                    start_date=start_date.strftime("%Y-%m-%d"),
                    end_date=end_date.strftime("%Y-%m-%d"),
                )
            ],
        )
        
        response = client.run_report(request)
        logger.info(f"GA4からのレスポンスを受信: {len(response.rows)} 行のデータ")
        
        # レスポンスをディクショナリに変換
        metrics_dict = {}
        for row in response.rows:
            path = row.dimension_values[0].value
            # パスを正規化
            if not path.startswith('/'):
                path = '/' + path
            if not path.endswith('/'):
                path = path + '/'
            
            # /share-deepresearch/ プレフィックスを削除
            path = path.replace('/share-deepresearch', '')
                
            logger.debug(f"GA4から取得したパス: {path}")  # デバッグログを追加
            metrics_dict[path] = {
                "pageViews": int(row.metric_values[0].value),
                "users": int(row.metric_values[1].value),
                "avgSessionDuration": float(row.metric_values[2].value)
            }
        
        logger.info(f"メトリクスの変換完了: {len(metrics_dict)} ページのデータを処理")
        # 取得したすべてのパスをログ出力
        logger.info(f"取得したパス一覧: {list(metrics_dict.keys())}")
        return metrics_dict
    except Exception as e:
        logger.error(f"GA4メトリクスの取得中にエラーが発生: {str(e)}")
        raise

def update_markdown_files(metrics_dict):
    # _topics配下の全てのindex.mdファイルを取得
    md_files = glob.glob("_topics/**/index.md", recursive=True)
    logger.info(f"更新対象のMarkdownファイル数: {len(md_files)}")
    
    updated_files = 0
    for md_file in md_files:
        try:
            # ファイルのパスからURLパスを生成
            file_path = Path(md_file)
            url_path = f"/topics/{str(file_path.parent.name)}/index/"
            
            # GA4のメトリクスに含まれるパスバリエーションを試す
            possible_paths = [
                url_path,  # /topics/folder-name/index/
                url_path[:-1],  # /topics/folder-name/index
                url_path.lower(),  # /topics/folder-name/index/ (小文字)
                url_path.lower()[:-1],  # /topics/folder-name/index (小文字)
                f"/topics/{str(file_path.parent.name)}/",  # /topics/folder-name/
                f"/topics/{str(file_path.parent.name)}",  # /topics/folder-name
            ]
            
            matched_path = None
            for path in possible_paths:
                if path in metrics_dict:
                    matched_path = path
                    break
            
            if matched_path:
                logger.info(f"ファイルを更新中: {md_file} (マッチしたパス: {matched_path})")
                # Front Matterを更新
                post = frontmatter.load(md_file)
                metrics = metrics_dict[matched_path]
                
                post["ga4_metrics"] = {
                    "pageViews": metrics["pageViews"],
                    "users": metrics["users"],
                    "avgSessionDuration": metrics["avgSessionDuration"]
                }
            else:
                logger.warning(f"メトリクスが見つかりません: {url_path} ({md_file})")
                logger.debug(f"試行したパス: {possible_paths}")
                # Front Matterを更新（すべての値を0に設定）
                post = frontmatter.load(md_file)
                post["ga4_metrics"] = {
                    "pageViews": 0,
                    "users": 0,
                    "avgSessionDuration": 0.0
                }
                logger.info(f"メトリクスを0に設定: {md_file}")
            # ファイルを保存（最後に改行を追加）
            with open(md_file, 'wb') as f:
                frontmatter.dump(post, f)
                f.write(b'\n')  # 最後に改行を追加
            updated_files += 1
            logger.info(f"ファイルの更新完了: {md_file}")
        except Exception as e:
            logger.error(f"ファイル {md_file} の更新中にエラーが発生: {str(e)}")
    
    logger.info(f"更新完了: {updated_files} ファイルを更新")

def main():
    try:
        logger.info("スクリプトの実行を開始")
        
        property_id = os.environ.get("GA4_PROPERTY_ID", "")
        credentials_json = os.environ.get("GA4_CREDENTIALS_JSON", "")
        
        if not property_id or not credentials_json:
            logger.error("環境変数が設定されていません: GA4_PROPERTY_ID または GA4_CREDENTIALS_JSON が未設定")
            return
        
        logger.info("GA4の認証情報を確認")
        
        # GA4から指標を取得
        metrics = get_ga4_metrics(property_id, credentials_json)
        
        # Markdownファイルを更新
        update_markdown_files(metrics)
        
        logger.info("スクリプトの実行が正常に完了")
    except Exception as e:
        logger.error(f"予期せぬエラーが発生: {str(e)}")
        raise

if __name__ == "__main__":
    main()
