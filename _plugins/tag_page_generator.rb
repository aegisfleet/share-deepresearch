module Jekyll
  class TagPageGenerator < Generator
    safe true

    def generate(site)
      tags = site.posts.docs.flat_map { |post| post.data['tags'] || [] }.uniq

      tags.each do |tag|
        site.pages << TagPage.new(site, site.source, File.join('tags', tag), tag, site.posts.docs.select { |post| (post.data['tags'] || []).include?(tag) })
      end
    end
  end

  class TagPage < Page
    def initialize(site, base, dir, tag, posts)
      @site = site
      @base = base
      @dir  = dir
      @name = 'index.html'

      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'tag_page.html') # This will be created in the next step
      self.data['tag'] = tag
      self.data['title'] = "Posts tagged "#{tag}""
      self.data['posts'] = posts
      self.data['layout'] = 'tag_page' # Ensure this matches the layout filename
    end
  end
end
