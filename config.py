#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

"""QQ机器人配置文件"""

# 基础配置 - QQ开发者平台相关
appid = os.getenv("ROBOT_APPID", "")                              # 机器人APPID，在QQ开发者平台获取
secret = os.getenv("ROBOT_SECRET", "")      # 机器人密钥
ROBOT_QQ = os.getenv("ROBOT_QQ", "")                          # 机器人QQ号
IMAGE_BED_CHANNEL_ID = os.getenv("IMAGE_BED_CHANNEL_ID", "")                 # 图床频道子频道ID，用于图床上传
OWNER_IDS = os.getenv("OWNER_IDS", "").split(",") if os.getenv("OWNER_IDS") else [""] # 主人OPENID列表，可使用仅主人插件

# 消息处理配置 - 控制消息格式和行为
USE_MARKDOWN = os.getenv("USE_MARKDOWN", "False").lower() == "true"                             # 是否使用Markdown格式发送消息 MD模板请使用False
HIDE_AVATAR_GLOBAL = os.getenv("HIDE_AVATAR_GLOBAL", "False").lower() == "true"                        # 全局启用Markdown无头像模式（私聊可用）
SEND_DEFAULT_RESPONSE = os.getenv("SEND_DEFAULT_RESPONSE", "False").lower() == "true"                     # 无匹配命令时是否发送默认回复
DEFAULT_RESPONSE_EXCLUDED_REGEX = []             # 排除默认回复的消息正则表达式列表
MAINTENANCE_MODE = os.getenv("MAINTENANCE_MODE", "False").lower() == "true"                         # 维护模式开关，开启后机器人暂停服务
BLACKLIST_ENABLED = os.getenv("BLACKLIST_ENABLED", "True").lower() == "true"                         # 黑名单功能开关，关闭后黑名单用户能正常使用插件
GROUP_BLACKLIST_ENABLED = os.getenv("GROUP_BLACKLIST_ENABLED", "True").lower() == "true"  # 群黑名单功能开关，开启后黑名单群内所有消息都会发送群黑名单模板
ENABLE_WELCOME_MESSAGE = os.getenv("ENABLE_WELCOME_MESSAGE", "False").lower() == "true"                    # 是否启用入群欢迎消息功能
ENABLE_NEW_USER_WELCOME = os.getenv("ENABLE_NEW_USER_WELCOME", "False").lower() == "true"                   # 是否启用新用户首次交互欢迎
ENABLE_FRIEND_ADD_MESSAGE = os.getenv("ENABLE_FRIEND_ADD_MESSAGE", "False").lower() == "true"                 # 是否启用添加好友自动发送消息功能
SAVE_RAW_MESSAGE_TO_DB = os.getenv("SAVE_RAW_MESSAGE_TO_DB", "False").lower() == "true"                   # 是否将消息的原始内容存储到数据库中,开启后可能会数据库硬盘占用略微上涨

# 用户ID反转模式配置（可选） - 控制user_id和union_openid的使用
USE_UNION_ID_FOR_GROUP = os.getenv("USE_UNION_ID_FOR_GROUP", "False").lower() == "true"  # 群聊/私聊ID反转模式：True时user_id使用union_openid，union_openid使用原user_id；若union_openid为空则使用原user_id
USE_UNION_ID_FOR_CHANNEL = os.getenv("USE_UNION_ID_FOR_CHANNEL", "False").lower() == "true"  # 频道ID反转模式：True时user_id使用union_openid，union_openid使用原user_id；若union_openid为空则使用原user_id

# Markdown AJ万能模板配置 - 没有万能模板请留空
MARKDOWN_AJ_TEMPLATE = {
    'template_id': os.getenv("MARKDOWN_AJ_TEMPLATE_ID", "1"),  # AJ 模板 ID
    'keys': os.getenv("MARKDOWN_AJ_KEYS", "a,b,c,d,e,f,g,h,i,j"),  # 模板参数键名，使用逗号分割
}

# 服务器配置 - HTTP服务相关设置
SERVER_CONFIG = {
    'host': os.getenv("SERVER_HOST", "0.0.0.0"),  # HTTP服务监听地址
    'port': int(os.getenv("SERVER_PORT", 5001)),  # HTTP服务监听端口号
}

# WebSocket配置 - 实时通信连接设置
WEBSOCKET_CONFIG = {
    'enabled': os.getenv("WEBSOCKET_ENABLED", "True").lower() == "true",  # 是否启用WebSocket连接功能
    'custom_url': os.getenv("WEBSOCKET_CUSTOM_URL", None),  # 自定义WebSocket连接地址
    'log_level': os.getenv("WEBSOCKET_LOG_LEVEL", "INFO"),  # WebSocket专用日志级别
    'log_message_content': os.getenv("WEBSOCKET_LOG_MESSAGE_CONTENT", "False").lower() == "true",  # 是否记录消息内容
}

# Web面板配置 - 安全控制和界面外观设置
WEB_CONFIG = {
    'access_token': os.getenv("WEB_ACCESS_TOKEN", "admin"),  # Web面板访问令牌
    'admin_password': os.getenv("WEB_ADMIN_PASSWORD", "admin"),  # 管理员登录密码
    'framework_name': os.getenv("WEB_FRAMEWORK_NAME", "Elaina"),  # 框架名称
    'favicon_url': os.getenv("WEB_FAVICON_URL", f'https://q1.qlogo.cn/g?b=qq&nk={ROBOT_QQ}&s=100'),  # 网页图标URL
    'pc_title_suffix': os.getenv("WEB_PC_TITLE_SUFFIX", "仪表盘"),  # PC端标题后缀
    'login_title_suffix': os.getenv("WEB_LOGIN_TITLE_SUFFIX", "面板"),  # 登录页面标题后缀
}

# 日志数据库配置 - 系统日志存储设置
LOG_DB_CONFIG = {
    'host': os.getenv("DB_HOST", "127.0.0.1"),
    'port': int(os.getenv("DB_PORT", 3306)),
    'user': os.getenv("DB_USER", "root"),
    'password': os.getenv("DB_PASSWORD", ""),
    'database': os.getenv("DB_DATABASE", "elainabot"),
    'insert_interval': 2,
    'batch_size': 1000,
    'table_prefix': f"{appid}_",
    'retention_days': 5,
    'max_retry': 3,
    'retry_interval': 2,
    'initial_load_count': 50,
}

# 主数据库配置 - 业务数据存储设置
DB_CONFIG = {
    'enabled': os.getenv("DB_ENABLED", "True").lower() == "true",
    'host': os.getenv("DB_HOST", "127.0.0.1"),
    'port': int(os.getenv("DB_PORT", 3306)),
    'user': os.getenv("DB_USER", "root"),
    'password': os.getenv("DB_PASSWORD", ""),
    'database': os.getenv("DB_DATABASE", "elainabot"),
    'min_pool_size': 5,
    'connect_timeout': 5,
    'read_timeout': 3,
    'write_timeout': 3,
    'autocommit': True,
    'connection_lifetime': 300,
    'retry_count': 3,
    'retry_interval': 0.5,
}

# Redis缓存配置
REDIS_CONFIG = {
    'enabled': os.getenv("REDIS_ENABLED", "False").lower() == "true",
    'host': os.getenv("REDIS_HOST", "127.0.0.1"),
    'port': int(os.getenv("REDIS_PORT", 6379)),
    'password': os.getenv("REDIS_PASSWORD", None),
    'db': int(os.getenv("REDIS_DB", 0)),
    'max_connections': 50,
    'socket_timeout': 5,
    'socket_connect_timeout': 5,
    'retry_on_timeout': True,
    'health_check_interval': 30,
    'decode_responses': True,
}

# 腾讯云COS对象存储配置
COS_CONFIG = {
    'enabled': os.getenv("COS_ENABLED", "False").lower() == "true",
    'secret_id': os.getenv("COS_SECRET_ID", ""),
    'secret_key': os.getenv("COS_SECRET_KEY", ""),
    'region': os.getenv("COS_REGION", "ap-guangzhou"),
    'bucket_name': os.getenv("COS_BUCKET_NAME", ""),
    'domain': os.getenv("COS_DOMAIN", None),
    'upload_path_prefix': os.getenv("COS_UPLOAD_PATH_PREFIX", "meme/"),
    'max_file_size': 30 * 1024 * 1024,
}

# Bilibili图床配置
BILIBILI_IMAGE_BED_CONFIG = {
    'enabled': os.getenv("BILIBILI_ENABLED", "False").lower() == "true",
    'csrf_token': os.getenv("BILIBILI_CSRF_TOKEN", ""),
    'sessdata': os.getenv("BILIBILI_SESSDATA", ""),
    'bucket': "openplatform",
}

# 文件保护配置
PROTECTED_FILES = [
    "config.py",
    "core/event/markdown_templates.py",
    "core/plugin/message_templates.py",
    "plugins/",
]
