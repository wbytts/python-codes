import xmlrpc.client
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class BlogInfo:
    """博客信息结构"""

    def __init__(self, **options):
        self.blog_id = options.get('blog_id')
        self.url = options.get('url')
        self.blogName = options.get('blogName')


class Post:
    """博客结构"""

    def __init__(self, **options):
        # 创建日期，当发布的时候需要
        self.dateCreated = options.get('dateCreated')
        # 描述信息，当发布的时候需要
        self.description = options.get('description')
        # 标题，当发布的时候需要
        self.title = options.get('title')
        # 分类，可选，下面都是可选的~~~
        self.categories = options.get('categories')
        self.enclosure = options.get('enclosure')
        self.link = options.get('link')
        self.permalink = options.get('permalink')
        self.postid = options.get('postid')
        self.source = options.get('source')
        self.userid = options.get('userid')
        self.mt_allow_comments = options.get('mt_allow_comments')
        self.mt_allow_pings = options.get('mt_allow_pings')
        self.mt_convert_breaks = options.get('mt_convert_breaks')
        self.mt_text_more = options.get('mt_text_more')
        self.mt_excerpt = options.get('mt_excerpt')
        self.mt_keywords = options.get('mt_keywords')
        self.wp_slug = options.get('wp_slug')

    def get_struct(self):
        # 基本信息，发布时必传
        struct = {
            "dateCreated": self.dateCreated,
            "description": self.description,
            "title": self.title,
        }
        # 可选信息
        # 分类
        if self.categories != None: struct['categories'] = self.categories
        if self.enclosure != None: struct['enclosure'] = self.enclosure
        if self.link != None: struct['link'] = self.link
        if self.permalink != None: struct['permalink'] = self.permalink
        if self.postid != None: struct['postid'] = self.postid
        if self.source != None: struct['source'] = self.source
        if self.userid != None: struct['userid'] = self.userid
        # s是否允许评论
        if self.mt_allow_comments != None: struct['mt_allow_comments'] = self.mt_allow_comments
        if self.mt_allow_pings != None: struct['mt_allow_pings'] = self.mt_allow_pings
        if self.mt_convert_breaks != None: struct['mt_convert_breaks'] = self.mt_convert_breaks
        if self.mt_text_more != None: struct['mt_text_more'] = self.mt_text_more
        if self.mt_excerpt != None: struct['mt_excerpt'] = self.mt_excerpt
        # 关键词
        if self.mt_keywords != None: struct['mt_keywords'] = self.mt_keywords
        if self.wp_slug != None: struct['wp_slug'] = self.wp_slug
        return struct


class CategoryInfo:
    """分类结构"""

    def __init__(self, **options):
        self.decription = options.get('decription')
        self.htmlUrl = options.get('html_url')
        self.rssUrl = options.get('rss_url')
        self.title = options.get('title')
        self.categoryid = options.get('category_id')


class FileData:
    """文件数据结构"""

    def __init__(self, options):
        self.bits = options.get('bits')
        self.name = options.get('name')
        self.type = options.get('type')


class UrlData:
    """URL结构"""

    def __init__(self, **options):
        self.ur = options.get('url')


class Enclosure:
    def __init__(self, **options):
        self.length = options.get('length')
        self.type = options.get('type')
        self.url = options.get('url')


class Source:
    def __init__(self, **options):
        self.name = options.get('name')
        self.url = options.get('url')


class MetaWeblog:
    """
    MetaWeblog客户端类
    """

    def __init__(self, url, username, password):
        """
        初始化博客信息
        :param url: metaWeblog接口地址
        :param username:用户名
        :param password:密码
        """
        self.url, self.username, self.password = url, username, password
        self.proxy = xmlrpc.client.ServerProxy(self.url)

    def delete_post(self, post_id, publish=None):
        """
        删除一篇博客
        :param post_id:博客id
        :param publish:在适用的情况下，它指定在帖子被删除后是否应该重新发布博客
        :return:总是返回 True
        """
        return self.proxy.blogger.deletePost(self.url, post_id, self.username, self.password, publish)

    def get_users_blogs(self):
        """
        获取博客的基本信息
        :return: [{'blogid': '445714', 'url': 'https://www.cnblogs.com/wbyixx/', 'blogName': 'Aloys Wang'}]
        """
        return self.proxy.blogger.getUsersBlogs(self.url, self.username, self.password)

    def edit_post(self, post_id, post, publish=None):
        """
        编辑博客文章
        :param post_id:博客id
        :param post: 博客实体
        :param publish: 是否发布
        :return: any
        """
        return self.proxy.metaWeblog.editPost(post_id, self.username, self.password, post, publish)

    def get_categories(self, blog_id):
        """
        获取分类
        :param blog_id: 博客id
        :return: 分类信息实体数组
        """
        return self.proxy.metaWeblog.getCategories(blog_id)

    def get_post(self, blog_id):
        """
        获取一篇博客的详情
        :param blog_id: 博客id
        :return: 博客字典对象
        """
        return self.proxy.metaWeblog.getPost(blog_id, self.username, self.password)

    def get_recent_posts(self, count, start_blog_id=''):
        """
        获取历史文章列表
        :param count: 要获取的博客的个数
        :param start_blog_id: 获取的起始id
        :return: 博客字典对象的列表
        """
        return self.proxy.metaWeblog.getRecentPosts(start_blog_id, self.username, self.password, count)

    def new_media_object(self, blog_id, file):
        """
        在指定的博客中创建一个新文件
        :param blog_id:博客id
        :param file:文件结构
        :return:以结构的字符串形式返回url
        """
        return self.proxy.metaWeblog.newMediaObject(blog_id, self.username, self.password, file)

    def new_post(self, post, blog_id='', publish=True):
        """
        新博客
        :param blog_id: 博客id
        :param post: 博客结构体
        :param publish: 是否发布
        :return:string
        """
        return self.proxy.metaWeblog.newPost(blog_id, self.username, self.password, post, publish)

    def new_category(self, blog_id, category):
        """
        新建分类
        :param blog_id:博客id
        :param category: 分类结构体
        :return:
        """
        return self.proxy.wp.newCategory(blog_id, self.username, self.password, category)
