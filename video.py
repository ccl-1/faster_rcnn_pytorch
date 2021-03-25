<!DOCTYPE html>
<html class="" lang="zh-CN">
<head prefix="og: http://ogp.me/ns#">
<meta charset="utf-8">
<link as="style" href="https://codechina.csdn.net/assets/application-fc8ddf8301aaa61b629b9ecdb9108c479082b907355ad58a42530545ec9b4e89.css" rel="preload">
<link as="style" href="https://codechina.csdn.net/assets/highlight/themes/white-6a22b8b375794a1289df4622d79144821592090a8477236097a5e6dacb004e68.css" rel="preload">

<meta content="IE=edge" http-equiv="X-UA-Compatible">

<meta content="object" property="og:type">
<meta content="CODE CHINA" property="og:site_name">
<meta content="video.py · master · mirrors / bubbliiiing / faster-rcnn-pytorch" property="og:title">
<meta content="🚀 Github 镜像仓库 🚀 源项目地址 ⬇ ⬇ " property="og:description">
<meta content="https://codechina.csdn.net/assets/gitlab_logo-42ec4452266baa0b5905cd1ef5fbee2f36d39d56ff6ba69b47ef09f90ae3ae85.png" property="og:image">
<meta content="64" property="og:image:width">
<meta content="64" property="og:image:height">
<meta content="https://codechina.csdn.net/mirrors/bubbliiiing/faster-rcnn-pytorch/-/blob/master/video.py" property="og:url">
<meta content="summary" property="twitter:card">
<meta content="video.py · master · mirrors / bubbliiiing / faster-rcnn-pytorch" property="twitter:title">
<meta content="🚀 Github 镜像仓库 🚀 源项目地址 ⬇ ⬇ " property="twitter:description">
<meta content="https://codechina.csdn.net/assets/gitlab_logo-42ec4452266baa0b5905cd1ef5fbee2f36d39d56ff6ba69b47ef09f90ae3ae85.png" property="twitter:image">

<title>video.py · master · mirrors / bubbliiiing / faster-rcnn-pytorch · CODE CHINA</title>
<meta content="🚀 Github 镜像仓库 🚀 源项目地址 ⬇ ⬇ " name="description">
<link rel="shortcut icon" type="image/png" href="/uploads/-/system/appearance/favicon/1/logo_icon.png" id="favicon" data-original-href="/uploads/-/system/appearance/favicon/1/logo_icon.png" />

<link rel="stylesheet" media="all" href="/assets/application-fc8ddf8301aaa61b629b9ecdb9108c479082b907355ad58a42530545ec9b4e89.css" />

<link rel="stylesheet" media="all" href="/assets/application_utilities-aca0b81ce4340412b8407966eef30a4182b51178a2c547d30ad800a4fd84a6cb.css" />
<link rel="stylesheet" media="all" href="/assets/themes/theme_indigo-03d9edccaad40dfef1090b7e66f6232229610dc0e183c018f940e37ec37bd625.css" />

<link rel="stylesheet" media="all" href="/assets/highlight/themes/white-6a22b8b375794a1289df4622d79144821592090a8477236097a5e6dacb004e68.css" />


<script nonce="LJ1GF0JLE5/YK+EOtU8Bdw==">
//<![CDATA[
window.gon={};
//]]>
</script>
<script src="/assets/locale/zh_CN/app-b339ef26e1c5ce7a54a8df6a9a0309309e3e3c91b2022f03b79ff8705578b06c.js" defer="defer" nonce="LJ1GF0JLE5/YK+EOtU8Bdw=="></script>


<script src="/assets/webpack/runtime.7eae5e18.bundle.js" defer="defer" nonce="LJ1GF0JLE5/YK+EOtU8Bdw=="></script>
<script src="/assets/webpack/main.04bf6eed.chunk.js" defer="defer" nonce="LJ1GF0JLE5/YK+EOtU8Bdw=="></script>
<script src="/assets/webpack/commons-pages.projects-pages.projects.activity-pages.projects.alert_management.details-pages.project-b9665fe9.9a9e13d3.chunk.js" defer="defer" nonce="LJ1GF0JLE5/YK+EOtU8Bdw=="></script>
<script src="/assets/webpack/commons-pages.admin.application_settings-pages.admin.application_settings.general-pages.admin.applic-d549e6f7.4df4e8eb.chunk.js" defer="defer" nonce="LJ1GF0JLE5/YK+EOtU8Bdw=="></script>
<script src="/assets/webpack/commons-pages.projects.blame.show-pages.projects.blob.show.863c65b1.chunk.js" defer="defer" nonce="LJ1GF0JLE5/YK+EOtU8Bdw=="></script>
<script src="/assets/webpack/pages.projects.blob.show.7a096a00.chunk.js" defer="defer" nonce="LJ1GF0JLE5/YK+EOtU8Bdw=="></script>

<script nonce="LJ1GF0JLE5/YK+EOtU8Bdw==">
//<![CDATA[
window.uploads_path = "/mirrors/bubbliiiing/faster-rcnn-pytorch/uploads";



//]]>
</script>
<meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="uSFOPFiXw5F/+3X9z7P0TX9pOo+/0OT2hcffv6Y7AwNAK3W5AACRAmPCMy0Xolu00wJzjcGyydv+ZJvo7waWQw==" />
<meta name="csp-nonce" content="LJ1GF0JLE5/YK+EOtU8Bdw==" />
<meta name="action-cable-url" content="/-/cable" />
<meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport">
<meta content="#474D57" name="theme-color">
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-iphone-5a9cee0e8a51212e70b90c87c12f382c428870c0ff67d1eb034d884b78d2dae7.png" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-ipad-a6eec6aeb9da138e507593b464fdac213047e49d3093fc30e90d9a995df83ba3.png" sizes="76x76" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-iphone-retina-72e2aadf86513a56e050e7f0f2355deaa19cc17ed97bbe5147847f2748e5a3e3.png" sizes="120x120" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-ipad-retina-8ebe416f5313483d9c1bc772b5bbe03ecad52a54eba443e5215a22caed2a16a2.png" sizes="152x152" />
<meta content="/assets/favicon-42ec4452266baa0b5905cd1ef5fbee2f36d39d56ff6ba69b47ef09f90ae3ae85.png" name="msapplication-TileImage">




</head>

<body class="ui-indigo tab-width-8  gl-browser-safari gl-platform-mac" data-find-file="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/find_file/master" data-group="bubbliiiing" data-namespace-id="16034" data-page="projects:blob:show" data-page-type-id="master/video.py" data-project="faster-rcnn-pytorch" data-project-id="4053">

<script nonce="LJ1GF0JLE5/YK+EOtU8Bdw==">
//<![CDATA[
gl = window.gl || {};
gl.client = {"isSafari":true,"isMac":true};


//]]>
</script>


<link rel="stylesheet" type="text/css" href="https://g.csdnimg.cn/user-login/2.2.8/css/??index.css,toast.style.css">
<script src="https://g.csdnimg.cn/??lib/jquery/1.12.4/jquery.min.js" type="text/javascript" charset="utf-8"></script>
<script type="text/javascript" src="https://g.csdnimg.cn/user-login/2.1.5/user-login.js"></script>
<script type="text/javascript" src="https://g.csdnimg.cn/user-login/2.2.4/js/??toast.script.js"></script>
<script src="https://g.csdnimg.cn/common/csdn-report/report.js" type="text/javascript"></script>
<header class="navbar navbar-gitlab navbar-expand-sm js-navbar" data-qa-selector="navbar">
<a class="sr-only gl-accessibility" href="#content-body" tabindex="1">Skip to content</a>
<div class="container-fluid">
<div class="header-content">
<div class="title-container">
<h1 class="title">
<a title="仪表板" id="logo" href="/dashboard/projects/home"><img class="brand-header-logo lazy" data-src="/uploads/-/system/appearance/header_logo/1/3-1_%E7%94%BB%E6%9D%BF_1_copy.png" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" />
</a></h1>
<ul class="list-unstyled navbar-sub-nav">
<li class="d-md-block home dropdown header-groups qa-groups-dropdown open-source-show-button" data-toggle="tooltip" data-placement="bottom" data-container="body" data-track-label="groups_dropdown" data-track-event="click_dropdown" data-track-value=""><a title="开源广场" class="dashboard-shortcuts-topics abtn" href="/explore/welcome">开源广场
<svg class="s16 caret-down mobile-hide" data-testid="chevron-down-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#chevron-down"></use></svg>
</a><ul class="header-bar-subnav">
<li>
<a title="开源秀" aria-label="开源秀" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/lives">开源秀
</a></li>
<li>
<a title="学习广场" aria-label="学习广场" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/courses">学习广场
</a></li>
</ul>
</li><li class="mobile-show home dropdown header-groups qa-groups-dropdown open-source-show-button" data-toggle="tooltip" data-placement="bottom" data-container="body" data-track-label="groups_dropdown" data-track-event="click_dropdown" data-track-value=""><a title="开源秀" aria-label="开源秀" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/lives">开源秀
</a></li><li id="nav-projects-dropdown" class="mobile-hide home dropdown header-projects qa-projects-dropdown" data-track-label="projects_dropdown" data-track-event="click_dropdown" data-track-value=""><button class="btn" data-toggle="dropdown" type="button">
项目
<svg class="s16 caret-down" data-testid="chevron-down-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#chevron-down"></use></svg>
</button>
<div class="dropdown-menu frequent-items-dropdown-menu">
<div class="frequent-items-dropdown-container">
<div class="frequent-items-dropdown-sidebar qa-projects-dropdown-sidebar">
<ul>
<li class=""><a class="qa-your-projects-link" href="/users/qq_36758461/projects">您的项目
</a></li><li class=""><a href="/users/qq_36758461/starred?show_starred_projects=true">Star项目
</a></li><li class=""><a href="/explore/projects/starred">浏览项目
</a></li></ul>
</div>
<div class="frequent-items-dropdown-content">
<div data-project-id="4053" data-project-name="faster-rcnn-pytorch" data-project-namespace="mirrors / bubbliiiing / faster-rcnn-pytorch" data-project-web-url="/mirrors/bubbliiiing/faster-rcnn-pytorch" data-user-name="qq_36758461" id="js-projects-dropdown"></div>
</div>
</div>

</div>
</li><li id="nav-groups-dropdown" class="mobile-hide home dropdown header-groups qa-groups-dropdown" data-track-label="groups_dropdown" data-track-event="click_dropdown" data-track-value=""><button class="btn" data-toggle="dropdown" type="button">
组织
<svg class="s16 caret-down" data-testid="chevron-down-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#chevron-down"></use></svg>
</button>
<div class="dropdown-menu frequent-items-dropdown-menu">
<div class="frequent-items-dropdown-container">
<div class="frequent-items-dropdown-sidebar qa-groups-dropdown-sidebar">
<ul>
<li class=""><a class="qa-your-groups-link" href="/users/qq_36758461/groups">您的组织
</a></li><li class=""><a data-track-label="groups_dropdown_explore_groups" data-track-event="click_link" href="/explore/groups">浏览组织
</a></li></ul>
</div>
<div class="frequent-items-dropdown-content">
<div data-user-name="qq_36758461" id="js-groups-dropdown"></div>
</div>
</div>

</div>
</li><li class="d-none d-md-block home dropdown header-groups qa-groups-dropdown" data-toggle="tooltip" data-placement="bottom" data-container="body" data-track-label="groups_dropdown" data-track-event="click_dropdown" data-track-value=""><a title="Issue" class="dashboard-shortcuts-issues abtn" aria-label="Issue" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/dashboard/issues?assignee_username=qq_36758461">Issue
<span class="badge badge-pill green-badge hidden">
0
</span>
</a></li><li class="d-none d-md-block home dropdown header-groups qa-groups-dropdown" data-toggle="tooltip" data-placement="bottom" data-container="body" data-track-label="groups_dropdown" data-track-event="click_dropdown" data-track-value=""><a title="合并请求" class="dashboard-shortcuts-merge_requests abtn" aria-label="合并请求" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/dashboard/merge_requests?assignee_username=qq_36758461">合并请求
<span class="badge badge-pill hidden merge-requests-count">
0
</span>
</a></li><li class="d-none d-md-block home dropdown header-groups qa-groups-dropdown" data-toggle="tooltip" data-placement="bottom" data-container="body" data-track-label="groups_dropdown" data-track-event="click_dropdown" data-track-value=""><a title="代码片段" class="dashboard-shortcuts-snippets abtn" aria-label="合并请求" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/-/snippets">代码片段
</a></li><li class="hidden">
<a class="dashboard-shortcuts-projects" href="/dashboard/projects">项目
</a></li>

<li class="nav-item d-none d-lg-block m-auto">
<div class="search search-form" data-track-event="activate_form_input" data-track-label="navbar_search" data-track-value="">
<form class="form-inline" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" /><div class="search-input-container">
<div class="search-input-wrap">
<div class="dropdown" data-url="/search/autocomplete">
<input type="search" name="search" id="search" placeholder="搜索或转到..." class="search-input dropdown-menu-toggle no-outline js-search-dashboard-options" spellcheck="false" autocomplete="off" data-issues-path="/dashboard/issues" data-mr-path="/dashboard/merge_requests" data-qa-selector="search_term_field" aria-label="搜索或转到..." />
<button class="hidden js-dropdown-search-toggle" data-toggle="dropdown" type="button"></button>
<div class="dropdown-menu dropdown-select" data-testid="dashboard-search-options">
<div class="dropdown-content"><ul>
<li class="dropdown-menu-empty-item">
<a>
正在加载...
</a>
</li>
</ul>
</div><div class="dropdown-loading"><div class="gl-spinner-container"><span class="gl-spinner gl-spinner-orange gl-spinner-md gl-mt-7" aria-label="加载中"></span></div></div>
</div>
<svg class="s16 search-icon" data-testid="search-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#search"></use></svg>
<svg class="s16 clear-icon js-clear-input" data-testid="close-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#close"></use></svg>
</div>
</div>
</div>
<input type="hidden" name="group_id" id="group_id" value="16034" class="js-search-group-options" data-group-path="bubbliiiing" data-name="bubbliiiing" data-issues-path="/groups/mirrors/bubbliiiing/-/issues" data-mr-path="/groups/mirrors/bubbliiiing/-/merge_requests" />
<input type="hidden" name="project_id" id="search_project_id" value="4053" class="js-search-project-options" data-project-path="faster-rcnn-pytorch" data-name="faster-rcnn-pytorch" data-issues-path="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/issues" data-mr-path="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/merge_requests" data-issues-disabled="false" />
<input type="hidden" name="scope" id="scope" />
<input type="hidden" name="search_code" id="search_code" value="true" />
<input type="hidden" name="snippets" id="snippets" value="false" />
<input type="hidden" name="repository_ref" id="repository_ref" value="master" />
<input type="hidden" name="nav_source" id="nav_source" value="navbar" />
<div class="search-autocomplete-opts hide" data-autocomplete-path="/search/autocomplete" data-autocomplete-project-id="4053" data-autocomplete-project-ref="master"></div>
</form></div>

</li>
</ul>

</div>
<div class="navbar-collapse collapse">
<ul class="nav navbar-nav">
<li class="user-counter"><a title="待办事项列表" aria-label="待办事项列表" class="shortcuts-todos" data-qa-selector="todos_shortcut_button" data-toggle="tooltip" data-placement="bottom" data-track-label="main_navigation" data-track-event="click_to_do_link" data-track-property="navigation" data-container="body" href="/dashboard/todos"><svg class="s16" data-testid="todo-done-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#todo-done"></use></svg>
<span class="badge badge-pill hidden js-todos-count todos-count">
0
</span>
</a></li><li class="header-new dropdown" data-track-event="click_dropdown" data-track-label="new_dropdown" data-track-value="">
<a class="header-new-dropdown-toggle has-tooltip qa-new-menu-toggle" id="js-onboarding-new-project-link" title="新建..." ref="tooltip" aria-label="新建..." data-toggle="dropdown" data-placement="bottom" data-container="body" data-display="static" href="/projects/new"><svg class="s16" data-testid="plus-square-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#plus-square"></use></svg>
<svg class="s16 caret-down" data-testid="chevron-down-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#chevron-down"></use></svg>
</a><div class="dropdown-menu dropdown-menu-right addgroup">
<ul>
<li class="dropdown-bold-header">
当前项目
</li>
<li><a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/issues/new">新建issue</a></li>
<li class="divider"></li>
<li class="dropdown-bold-header">CODE CHINA</li>
<li><a class="qa-global-new-project-link" href="/projects/new">新建项目</a></li>
<li><a href="/groups/new">新建组织</a></li>
<li><a class="qa-global-new-snippet-link" href="/-/snippets/new">新建代码片段</a></li>
</ul>
</div>
</li>

<li class="dropdown header-user js-nav-user-dropdown nav-item" data-qa-selector="user_menu" data-track-event="click_dropdown" data-track-label="profile_dropdown" data-track-value="">
<a class="header-user-dropdown-toggle" data-toggle="dropdown" href="/qq_36758461"><img width="23" height="23" class="header-user-avatar qa-user-avatar lazy" alt="索隆啊" data-src="https://profile.csdnimg.cn/F/6/8/1_qq_36758461" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" />

<svg class="s16 caret-down" data-testid="chevron-down-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#chevron-down"></use></svg>
</a><div class="dropdown-menu dropdown-menu-right addgroup">
<ul>
<li class="current-user">
<div class="user-name gl-font-weight-bold">
索隆啊
</div>
@qq_36758461
</li>
<li>
<button class="btn menu-item js-set-status-modal-trigger" type="button">
设置状态
</button>
</li>
<li>
<a class="profile-link" data-user="qq_36758461" href="/qq_36758461">我的主页</a>
</li>
<li>
<a data-qa-selector="settings_link" href="/-/profile">设置</a>
</li>


<li class="divider d-md-none"></li>
<li>
<a class="help-link" href="/codechina/help-docs/-/wikis/">帮助</a>
</li>
<li>
<a class="keyboard-shortcuts-link js-shortcuts-modal-trigger" href="javascript:;">快捷键</a>
</li>
<li>
<a class="sign-out-link" data-qa-selector="sign_out_link" rel="nofollow" data-method="post" href="/users/sign_out">退出</a>
</li>
</ul>

</div>
</li>
</ul>
</div>
<button class="navbar-toggler d-block d-sm-none" type="button">
<span class="sr-only">切换导航</span>
<svg class="s12 more-icon js-navbar-toggle-right" data-testid="ellipsis_h-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#ellipsis_h"></use></svg>
<svg class="s12 close-icon js-navbar-toggle-left" data-testid="close-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#close"></use></svg>
</button>
</div>
</div>
</header>
<div class="js-set-status-modal-wrapper" data-current-emoji="" data-current-message="" data-default-emoji="speech_balloon"></div>
<script src="/assets/drag_sort/sortable.min-b2de54b4d3ef84fe9656f624cc02d4b9b1d9754fb038148ff1fe06422b5f0f46.js" defer="defer" nonce="LJ1GF0JLE5/YK+EOtU8Bdw=="></script>
<script src="/assets/side_toolbar-b038a0be82a0c5d4553170b775867ea08ef8635b8fcc8374d3f48808f8dcf421.js" defer="defer" nonce="LJ1GF0JLE5/YK+EOtU8Bdw=="></script>

<div class="layout-page page-with-contextual-sidebar">
<nav class="breadcrumbs container-fluid container-limited mobile_breadcrumbs" role="navigation">
<div class="breadcrumbs-container">
<button name="button" type="button" class="toggle-mobile-nav"><span class="sr-only">打开侧边栏</span>
<svg class="s16" data-testid="hamburger-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#hamburger"></use></svg>
</button><div class="breadcrumbs-links js-title-container" data-qa-selector="breadcrumb_links_content">
<ul class="list-unstyled breadcrumbs-list js-breadcrumbs-list">
<li><a class="group-path breadcrumb-item-text js-breadcrumb-item-text " href="/mirrors">mirrors</a><svg class="s8 breadcrumbs-list-angle" data-testid="angle-right-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#angle-right"></use></svg></li><li><a class="group-path breadcrumb-item-text js-breadcrumb-item-text " href="/mirrors/bubbliiiing">bubbliiiing</a><svg class="s8 breadcrumbs-list-angle" data-testid="angle-right-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#angle-right"></use></svg></li> <li><a href="/mirrors/bubbliiiing/faster-rcnn-pytorch"><span class="breadcrumb-item-text js-breadcrumb-item-text">faster-rcnn-pytorch</span></a><svg class="s8 breadcrumbs-list-angle" data-testid="angle-right-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#angle-right"></use></svg></li>

<li>
<h2 class="breadcrumbs-sub-title">
<a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/blob/master/video.py">Repository</a>
</h2>
</li>
</ul>
</div>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"mirrors","item":"https://codechina.csdn.net/mirrors"},{"@type":"ListItem","position":2,"name":"bubbliiiing","item":"https://codechina.csdn.net/mirrors/bubbliiiing"},{"@type":"ListItem","position":3,"name":"faster-rcnn-pytorch","item":"https://codechina.csdn.net/mirrors/bubbliiiing/faster-rcnn-pytorch"},{"@type":"ListItem","position":4,"name":"Repository","item":"https://codechina.csdn.net/mirrors/bubbliiiing/faster-rcnn-pytorch/-/blob/master/video.py"}]}

</script>

</div>
</nav>

<div class="nav-sidebar">
<div class="nav-sidebar-inner-scroll">
<div class="context-header">
<a title="faster-rcnn-pytorch" href="/mirrors/bubbliiiing/faster-rcnn-pytorch"><div class="avatar-container rect-avatar s40 project-avatar">
<div class="avatar s40 avatar-tile identicon bg1">F</div>
</div>
<div class="sidebar-context-title">
faster-rcnn-pytorch
</div>
</a></div>
<ul class="sidebar-top-level-items qa-project-sidebar">
<li class="home"><a class="shortcuts-project rspec-project-link" data-qa-selector="project_link" href="/mirrors/bubbliiiing/faster-rcnn-pytorch"><div class="nav-icon-container">
<svg class="s16" data-testid="home-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#home"></use></svg>
</div>
<span class="nav-item-name">
项目概览
</span>
</a></li></ul>
</div>
</div>
<div class="js-show-on-project-root project-home-panel">
<div class="row gl-mb-3">
<div class="home-panel-title-row col-md-12 col-lg-8 d-flex">
<div class="d-flex flex-column flex-wrap align-items-baseline">
<div class="d-inline-flex align-items-baseline">
<h1 class="home-panel-title gl-mt-3 gl-mb-2" data-qa-selector="project_name_content">
<a href="/mirrors">mirrors</a> / <a href="/mirrors/bubbliiiing">bubbliiiing</a> / <a href="/mirrors/bubbliiiing/faster-rcnn-pytorch">faster-rcnn-pytorch</a>
<span class="access-request-links gl-ml-3">
<a class=".gl-pl-3.gl-border-l-1.gl-border-l-solid.gl-border-l-gray-500 applt-power" rel="nofollow" data-method="post" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/project_members/request_access">申请权限</a>

</span>

</h1>
</div>

</div>
</div>
<div class="project-repo-buttons col-md-12 col-lg-4 d-inline-flex flex-wrap justify-content-lg-end">
<div class="d-inline-flex">
<div class="js-notification-dropdown notification-dropdown home-panel-action-button gl-mt-3 gl-mr-3 dropdown inline" style="margin:0">
<form class="inline notification-form no-label" id="edit_notification_setting_164320" action="/-/notification_settings/164320" accept-charset="UTF-8" data-remote="true" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="patch" /><input type="hidden" name="project_id" id="project_id" value="4053" />
<input type="hidden" name="hide_label" id="hide_label" value="true" />
<input class="notification_setting_level" type="hidden" value="global" name="notification_setting[level]" id="notification_setting_level" />
<div class="d-inline-flex notification-btns">
<div class="js-notification-toggle-btns">
<div class="">
<button aria-label="通知设置 - 全局" class="btn btn-default btn-xs dropdown-new has-tooltip new-down-btn notifications-btn" data-container="body" data-flip="false" data-placement="top" data-target="dropdown-106312-4053-Project" data-toggle="dropdown" id="notifications-button" title="通知设置 - 全局" type="button">
<span class="new-down-left">
<svg class="s16 icon notifications-icon js-notifications-icon" data-testid="notifications-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#notifications"></use></svg>
</span>
<span class="js-notification-loading fa hidden"></span>
<span class="new-down-icon">
<svg class="s16 icon" data-testid="chevron-down-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#chevron-down"></use></svg>
</span>
</button>
<ul class="dropdown-106312-4053-Project dropdown-menu dropdown-menu-large dropdown-menu-no-wrap dropdown-menu-selectable" role="menu">
<li role="menuitem"><a class="update-notification is-active" data-notification-level="global" data-notification-title="全局" href="#"><strong class="dropdown-menu-inner-title">全局</strong><span class="dropdown-menu-inner-content">使用全局通知设置</span></a></li>
<li role="menuitem"><a class="update-notification " data-notification-level="watch" data-notification-title="关注" href="#"><strong class="dropdown-menu-inner-title">关注</strong><span class="dropdown-menu-inner-content">接收所有活动的通知</span></a></li>
<li role="menuitem"><a class="update-notification " data-notification-level="participating" data-notification-title="参与" href="#"><strong class="dropdown-menu-inner-title">参与</strong><span class="dropdown-menu-inner-content">只接收参与的讨论的通知</span></a></li>
<li role="menuitem"><a class="update-notification " data-notification-level="mention" data-notification-title="提及" href="#"><strong class="dropdown-menu-inner-title">提及</strong><span class="dropdown-menu-inner-content">只接收评论中提及(@)您的通知</span></a></li>
<li role="menuitem"><a class="update-notification " data-notification-level="disabled" data-notification-title="停用" href="#"><strong class="dropdown-menu-inner-title">停用</strong><span class="dropdown-menu-inner-content">不会收到任何通知邮件</span></a></li>
<li class="divider"></li>
<li>
<a class="update-notification" data-notification-level="custom" data-notification-title="Custom" data-target="#modal-106312-4053-Project" data-toggle="modal" href="#" role="button">
<strong class="dropdown-menu-inner-title">自定义</strong>
<span class="dropdown-menu-inner-content">只接收选择的事件通知</span>
</a>
</li>
</ul>

</div>
</div>
<span class="notification-count count-badge-count d-flex align-items-center">
<a title="关注用户" class="count" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/notificationers">87
</a></span>
</div>
</form></div>

</div>
<div class="count-buttons d-inline-flex">
<div class="count-badge d-inline-flex align-item-stretch gl-mr-3">
<button class="count-badge-button btn btn-default btn-xs d-flex align-items-center star-btn toggle-star" data-endpoint="/mirrors/bubbliiiing/faster-rcnn-pytorch/toggle_star.json" type="button">
<svg class="s16 icon" data-testid="star-o-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#star-o"></use></svg>
<span>Star</span>
</button>
<span class="star-count count-badge-count d-flex align-items-center">
<a title="Star用户" class="count" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/starrers">7
</a></span>
</div>

<div class="count-badge d-inline-flex align-item-stretch gl-mr-3">
<a class="btn btn-default btn-xs has-tooltip count-badge-button d-flex align-items-center fork-btn " href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/forks/new"><svg class="s16 icon" data-testid="fork-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#fork"></use></svg>
<span>Fork</span>
</a><span class="fork-count count-badge-count d-flex align-items-center">
<a title="Fork" class="count" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/forks">1
</a></span>
</div>

</div>
</div>
</div>
</div>

<style>
  .wiki-icon {
    display: none; }
</style>
<div class="head-nav-box">
<ul class="head-nav">
<li class="home active"><a class="shortcuts-project rspec-project-link" data-qa-selector="project_link" href="/mirrors/bubbliiiing/faster-rcnn-pytorch"><span>
代码
</span>
</a><ul class="subnav">
<li>
<a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/tree/master">文件
</a></li>
<li>
<a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/commits/master">提交
</a></li>
<li>
<a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/branches">分支
</a></li>
<li>
<a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/tags">Tags
</a></li>
<li>
<a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/graphs/master">贡献者
</a></li>
<li>
<a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/network/master">分支图
</a></li>
<li>
<a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/compare?from=master&amp;to=master">Diff
</a></li>
</ul>
</li><li class=""><a title="Issue" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/issues"><span>
Issue
<span class="project-num">
0
</span>
</span>
</a><ul class="subnav">
<li>
<a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/issues">列表
</a></li>
<li>
<a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/boards">看板
</a></li>
<li>
<a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/labels">标记
</a></li>
<li>
<a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/milestones">里程碑
</a></li>
</ul>
</li><li class=""><a class="shortcuts-merge_requests" data-qa-selector="merge_requests_link" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/merge_requests"><span>
合并请求
<span class="project-num">
0
</span>
</span>
</a></li><li class=""><a class="shortcuts-wiki" data-qa-selector="wiki_link" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/wikis/home"><div class="nav-icon-container wiki-icon">
<svg class="s16" data-testid="book-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#book"></use></svg>
</div>
<span class="nav-item-name">
Wiki
<span class="project-num">
0
</span>
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/wikis/home"><strong class="fly-out-top-item-name">
Wiki
</strong>
</a></li></ul>
</li>
<li class=""><a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/graphs/master/charts"><span>
分析
</span>
</a></li><li class=""><a title="成员" class="qa-members-link" id="js-onboarding-members-link" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/project_members"><span>
项目成员
</span>
</a></li><li class=""><a title="Pages" class="qa-pages-link" id="js-onboarding-pages-link" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/common_pages"><span>
Pages
</span>
</a></li></ul>
</div>

<div class="nav-sidebar">
<div class="nav-sidebar-inner-scroll">
<div class="context-header">
<a title="faster-rcnn-pytorch" href="/mirrors/bubbliiiing/faster-rcnn-pytorch"><div class="avatar-container rect-avatar s40 project-avatar">
<div class="avatar s40 avatar-tile identicon bg1">F</div>
</div>
<div class="sidebar-context-title">
faster-rcnn-pytorch
</div>
</a></div>
<ul class="sidebar-top-level-items qa-project-sidebar">
<li class="home"><a class="shortcuts-project rspec-project-link" data-qa-selector="project_link" href="/mirrors/bubbliiiing/faster-rcnn-pytorch"><div class="nav-icon-container">
<svg class="s16" data-testid="home-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#home"></use></svg>
</div>
<span class="nav-item-name">
项目概览
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/mirrors/bubbliiiing/faster-rcnn-pytorch"><strong class="fly-out-top-item-name">
项目概览
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="项目详情" class="shortcuts-project" href="/mirrors/bubbliiiing/faster-rcnn-pytorch"><span>详情</span>
</a></li><li class=""><a title="发布" class="shortcuts-project-releases" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/releases"><span>发布</span>
</a></li></ul>
</li><li class="active"><a class="shortcuts-tree" data-qa-selector="repository_link" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/tree/master"><div class="nav-icon-container">
<svg class="s16" data-testid="doc-text-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#doc-text"></use></svg>
</div>
<span class="nav-item-name" id="js-onboarding-repo-link">
仓库
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item active"><a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/tree/master"><strong class="fly-out-top-item-name">
仓库
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class="active"><a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/tree/master">文件
</a></li><li class=""><a id="js-onboarding-commits-link" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/commits/master">提交
</a></li><li class=""><a data-qa-selector="branches_link" id="js-onboarding-branches-link" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/branches">分支
</a></li><li class=""><a data-qa-selector="tags_link" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/tags">标签
</a></li><li class=""><a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/graphs/master">贡献者
</a></li><li class=""><a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/network/master">分支图
</a></li><li class=""><a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/compare?from=master&amp;to=master">比较
</a></li>
</ul>
</li><li class=""><a class="shortcuts-issues qa-issues-item" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/issues"><div class="nav-icon-container">
<svg class="s16" data-testid="issues-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#issues"></use></svg>
</div>
<span class="nav-item-name" id="js-onboarding-issues-link">
Issue
</span>
<span class="badge badge-pill count issue_counter">
0
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/issues"><strong class="fly-out-top-item-name">
Issue
</strong>
<span class="badge badge-pill count issue_counter fly-out-badge">
0
</span>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Issue" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/issues"><span>
列表
</span>
</a></li><li class=""><a title="看板" data-qa-selector="issue_boards_link" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/boards"><span>
看板
</span>
</a></li><li class=""><a title="标记" class="qa-labels-link" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/labels"><span>
标记
</span>
</a></li><li class=""><a title="里程碑" class="qa-milestones-link" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/milestones"><span>
里程碑
</span>
</a></li></ul>
</li><li class=""><a class="shortcuts-merge_requests" data-qa-selector="merge_requests_link" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/merge_requests"><div class="nav-icon-container">
<svg class="s16" data-testid="git-merge-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#git-merge"></use></svg>
</div>
<span class="nav-item-name" id="js-onboarding-mr-link">
合并请求
</span>
<span class="badge badge-pill count merge_counter js-merge-counter">
0
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/merge_requests"><strong class="fly-out-top-item-name">
合并请求
</strong>
<span class="badge badge-pill count merge_counter js-merge-counter fly-out-badge">
0
</span>
</a></li></ul>
</li>
<li class=""><a title="Pages" class="qa-pages-link" id="js-onboarding-pages-link" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/common_pages"><div class="nav-icon-container">
<svg class="s16" data-testid="rocket-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#rocket"></use></svg>
</div>
<span class="nav-item-name" id="js-onboarding-pipelines-link">
Pages
</span>
</a></li><li class=""><a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/graphs/master/charts"><div class="nav-icon-container">
<svg class="s16" data-testid="chart-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#chart"></use></svg>
</div>
<span class="nav-item-name" data-qa-selector="analytics_link">
分析
</span>
</a></li>
<li class=""><a class="shortcuts-wiki" data-qa-selector="wiki_link" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/wikis/home"><div class="nav-icon-container wiki-icon">
<svg class="s16" data-testid="book-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#book"></use></svg>
</div>
<span class="nav-item-name">
Wiki
<span class="project-num">
0
</span>
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/wikis/home"><strong class="fly-out-top-item-name">
Wiki
</strong>
</a></li></ul>
</li>
<li class=""><a title="成员" class="qa-members-link" id="js-onboarding-members-link" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/project_members"><div class="nav-icon-container">
<svg class="s16" data-testid="users-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#users"></use></svg>
</div>
<span class="nav-item-name">
成员
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/project_members"><strong class="fly-out-top-item-name">
成员
</strong>
</a></li></ul>
</li><a class="toggle-sidebar-button js-toggle-sidebar qa-toggle-sidebar rspec-toggle-sidebar" role="button" title="Toggle sidebar" type="button">
<svg class="s16 icon-chevron-double-lg-left" data-testid="chevron-double-lg-left-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#chevron-double-lg-left"></use></svg>
<svg class="s16 icon-chevron-double-lg-right" data-testid="chevron-double-lg-right-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#chevron-double-lg-right"></use></svg>
<span class="collapse-text">收起侧边栏</span>
</a>
<button name="button" type="button" class="close-nav-button"><svg class="s16" data-testid="close-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#close"></use></svg>
<span class="collapse-text">关闭侧边栏</span>
</button>
<li class="hidden">
<a title="动态" class="shortcuts-project-activity" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/activity"><span>
动态
</span>
</a></li>
<li class="hidden">
<a title="网络" class="shortcuts-network" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/network/master">分支图
</a></li>
<li class="hidden">
<a class="shortcuts-new-issue" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/issues/new">创建新Issue
</a></li>
<li class="hidden">
<a title="提交" class="shortcuts-commits" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/commits/master">提交
</a></li>
<li class="hidden">
<a title="Issue看板" class="shortcuts-issue-boards" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/boards">Issue看板</a>
</li>
</ul>
</div>
</div>


<div class="content-wrapper">
<div class="mobile-overlay"></div>

<div class="alert-wrapper gl-force-block-formatting-context">



<div class="broadcast-message alert-warning broadcast-banner-message  js-broadcast-notification-5 gl-display-flex" dir="auto" style="background-color: #44AD8E; color: #ffffff">
<div class="gl-flex-grow-1 gl-text-right gl-pr-3">
<svg class="s16 vertical-align-text-top" data-testid="bullhorn-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#bullhorn"></use></svg>
</div>
<div class="container-limited">
<p>该项目已经收录在 Github 加速计划中，访问速度提升10倍，每日同步更新。<a href="https://codechina.csdn.net/codechina/mirrors-settings/-/wikis/home?utm_source=mirror-banner">了解更多</a></p>
</div>
<div class="gl-flex-grow-1 gl-flex-basis-0 gl-text-right">
</div>
</div>










<div class="alert alert-warning hide" id="unCheckEmailAlert" role="alert" style="margin-left:16px;margin-right:16px">
你好, 索隆啊
由于您当前未设置邮箱地址，将无法使用CODE CHINA服务，
<a class="js-open-email-box" href="javascript:;">点击补充邮箱信息，
</a><a class="js-logout-btn" data-qa-selector="sign_out_link" rel="nofollow" data-method="delete" href="/sign_out?requestUrl=%2Fsign_in">切换账号登录。
</a></div>
<div class="alert alert-primary alert-dismissible fade show" data-dismiss="alert" id="checkEmailAlert" role="alert" style="display:none;margin-left:16px;margin-right:16px">
您的邮箱已经设置成功。
<button aria-label="close" class="close" data-dismiss="alert" style="line-height:0.7" type="button">
<span aria-hidden="true">
&times;
</span>
</button>
</div>
<div aria-hidden="true" aria-labelledby="inputEmailDialogLabel" class="modal" id="inputEmailDialog" role="dialog" tabindex="-1">
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<h3 class="modal-title" id="inputEmailDialogLabel">
设置邮箱
</h3>
<button aria-label="关闭" class="close" data-dismiss="modal" type="button">
<span aria-hidden>&times;</span>
</button>
</div>
<div class="modal-body">
CODE CHINA服务需要使用你的邮箱，请设置您的常用邮箱
<form id="emailForm">
<div class="form-group">
<label for="useremail">
请填写您的常用邮箱
</label>
<input class="form-control" id="useremail" placeholder="email@example.com" type="email">
</div>
</form>
<div class="err-msg">
请输入正确邮箱地址
</div>
</div>
<div class="modal-footer">
<button class="btn btn-secondary" data-dismiss="modal" type="button">
关闭
</button>
<button class="btn btn-primary js-set-email" type="button">
保存
</button>
</div>
</div>
</div>
</div>

<div class="d-flex"></div>
</div>
<div class="container-fluid container-limited ">
<div class="content" id="content-body">
<div class="flash-container flash-container-page sticky" data-qa-selector="flash_container">
</div>

<div class="js-signature-container" data-signatures-path="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/commits/2ec4edf01a2595d6971ee8901cf9e12ecde657cf/signatures?limit=1"></div>

<div class="tree-holder" id="tree-holder">
<div class="nav-block">
<div class="tree-ref-container">
<div class="tree-ref-holder">
<style>
  .qa-branches-select {
    height: 34px;
  }
</style>
<form class="project-refs-form" action="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/refs/switch" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="destination" id="destination" value="blob" />
<input type="hidden" name="path" id="path" value="video.py" />
<div class="dropdown branches-dropdown">
<button class="dropdown-menu-toggle js-project-refs-dropdown qa-branches-select" type="button" data-toggle="dropdown" data-selected="master" data-ref="master" data-refs-url="/mirrors/bubbliiiing/faster-rcnn-pytorch/refs?sort=updated_desc" data-field-name="ref" data-submit-form-on-click="true" data-visit="true"><span class="dropdown-toggle-text ">master</span><svg class="s16 dropdown-menu-toggle-icon gl-top-3" data-testid="chevron-down-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#chevron-down"></use></svg></button>
<div class="dropdown-menu dropdown-menu-paging dropdown-menu-selectable git-revision-dropdown qa-branches-dropdown">
<div class="dropdown-page-one">
<div class="dropdown-title gl-display-flex"><span class="gl-ml-auto">切换分支/标签</span><button class="dropdown-title-button dropdown-menu-close gl-ml-auto" aria-label="Close" type="button"><svg class="s16 dropdown-menu-close-icon" data-testid="close-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#close"></use></svg></button></div>
<div class="dropdown-input"><input type="search" id="" class="dropdown-input-field qa-dropdown-input-field" placeholder="搜索分支和标签" autocomplete="off" /><svg class="s16 dropdown-input-search" data-testid="search-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#search"></use></svg><svg class="s16 dropdown-input-clear js-dropdown-input-clear" data-testid="close-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#close"></use></svg></div>
<div class="dropdown-content"></div>
<div class="dropdown-loading"><div class="gl-spinner-container"><span class="gl-spinner gl-spinner-orange gl-spinner-md gl-mt-7" aria-label="加载中"></span></div></div>
</div>
</div>
</div>
</form>
</div>
<ul class="breadcrumb repo-breadcrumb">
<li class="breadcrumb-item">
<a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/tree/master">faster-rcnn-pytorch
</a></li>
<li class="breadcrumb-item">
<a href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/blob/master/video.py"><strong>video.py</strong>
</a></li>
</ul>
</div>
<div class="tree-controls gl-children-ml-sm-3"><a class="gl-button btn shortcuts-find-file" rel="nofollow" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/find_file/master">查找文件
</a><a class="btn js-blob-blame-link" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/blame/master/video.py">Blame</a><a class="btn" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/commits/master/video.py">历史</a><a class="btn js-data-file-blob-permalink-url" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/blob/dde6339c64ce998e6b447a3a9bf8d271d71f2ba6/video.py">永久链接</a><a class="gl-button btn js-data-file-blob-permalink-url" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/blob/dde6339c64ce998e6b447a3a9bf8d271d71f2ba6/video.py">Permalink</a></div>
</div>

<div class="info-well d-none d-sm-block">
<div class="well-segment">
<ul class="blob-commit-info">
<li class="commit flex-row js-toggle-container" id="commit-2ec4edf0">
<div class="avatar-cell d-none d-sm-block">
<a href="mailto:47347516%2Bbubbliiiing@users.noreply.github.com"><img alt="Bubbliiiing&#39;s avatar" src="https://secure.gravatar.com/avatar/0a131b6944605d6cc5a03924c47d00b5?s=80&amp;d=identicon" class="avatar s40 d-none d-sm-inline-block" title="Bubbliiiing" /></a>
</div>
<div class="commit-detail flex-list">
<div class="commit-content" data-qa-selector="commit_content">
<a class="commit-row-message item-title js-onboarding-commit-item " href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/commit/2ec4edf01a2595d6971ee8901cf9e12ecde657cf">Update video.py</a>
<span class="commit-row-message d-inline d-sm-none">
&middot;
2ec4edf0
</span>
<div class="committer">
由 <a class="commit-author-link" href="mailto:47347516%2Bbubbliiiing@users.noreply.github.com">Bubbliiiing</a> 提交于 <time class="js-timeago" title="8月 5, 2020 1:18下午" datetime="2020-08-05T05:18:02Z" data-toggle="tooltip" data-placement="bottom" data-container="body">8月 05, 2020</time>
</div>

</div>
<div class="commit-actions flex-row">
<button class="btn gpg-status-box js-loading-gpg-badge" data-commit-sha="2ec4edf01a2595d6971ee8901cf9e12ecde657cf" data-placement="top" data-title="GPG签名(加载中...)" data-toggle="tooltip" tabindex="0"></button>

<div class="commit-sha-group btn-group d-none d-sm-flex">
<div class="label label-monospace monospace">
2ec4edf0
</div>
<button class="btn gl-button btn btn-default" data-toggle="tooltip" data-placement="bottom" data-container="body" data-title="复制提交SHA" data-class="gl-button btn btn-default" data-clipboard-text="2ec4edf01a2595d6971ee8901cf9e12ecde657cf" type="button" title="复制提交SHA" aria-label="复制提交SHA"><svg class="s16" data-testid="copy-to-clipboard-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#copy-to-clipboard"></use></svg></button>

</div>
</div>
</div>
</li>

</ul>
</div>


</div>
<div class="blob-content-holder" id="blob-content-holder">
<article class="file-holder">
<div class="js-file-title file-title-flex-parent">
<div class="file-header-content">
<svg class="s16" data-testid="doc-text-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#doc-text"></use></svg>
<strong class="file-title-name gl-word-break-all" data-qa-selector="file_name_content">
video.py
</strong>
<button class="btn btn-clipboard btn-transparent" data-toggle="tooltip" data-placement="bottom" data-container="body" data-class="btn-clipboard btn-transparent" data-title="复制文件路径" data-clipboard-text="{&quot;text&quot;:&quot;video.py&quot;,&quot;gfm&quot;:&quot;`video.py`&quot;}" type="button" title="复制文件路径" aria-label="复制文件路径"><svg class="s16" data-testid="copy-to-clipboard-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#copy-to-clipboard"></use></svg></button>
<small class="mr-1">
1.0 KB
</small>
</div>

<div class="file-actions gl-display-flex gl-flex-fill-1 gl-align-self-start gl-md-justify-content-end"><button name="button" type="submit" class="btn btn-primary js-edit-blob js-critical-verification ml-2  js-edit-blob-link-fork-toggler" data-action="edit" data-fork-path="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/forks?continue%5Bnotice%5D=%E6%82%A8%E4%B8%8D%E8%83%BD%E7%9B%B4%E6%8E%A5%E5%AF%B9%E6%AD%A4%E9%A1%B9%E7%9B%AE%E8%BF%9B%E8%A1%8C%E6%9B%B4%E6%94%B9%E3%80%82%E6%AD%A4%E9%A1%B9%E7%9B%AE%E7%9A%84Fork%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E5%88%9B%E5%BB%BA%EF%BC%8C%E6%82%A8%E5%8F%AF%E4%BB%A5%E5%9C%A8Fork%E9%A1%B9%E7%9B%AE%E4%B8%AD%E8%BF%9B%E8%A1%8C%E6%9B%B4%E6%94%B9%EF%BC%8C%E4%BB%A5%E4%BE%BF%E6%8F%90%E4%BA%A4%E5%90%88%E5%B9%B6%E8%AF%B7%E6%B1%82%E3%80%82&amp;continue%5Bnotice_now%5D=%E6%82%A8%E4%B8%8D%E8%83%BD%E7%9B%B4%E6%8E%A5%E5%AF%B9%E6%AD%A4%E9%A1%B9%E7%9B%AE%E8%BF%9B%E8%A1%8C%E6%9B%B4%E6%94%B9%E3%80%82%E6%AD%A4%E9%A1%B9%E7%9B%AE%E7%9A%84Fork%E9%A1%B9%E7%9B%AE%E6%AD%A3%E5%9C%A8%E5%88%9B%E5%BB%BA%EF%BC%8C%E6%82%A8%E5%8F%AF%E4%BB%A5%E5%9C%A8Fork%E9%A1%B9%E7%9B%AE%E4%B8%AD%E8%BF%9B%E8%A1%8C%E6%9B%B4%E6%94%B9%EF%BC%8C%E4%BB%A5%E4%BE%BF%E6%8F%90%E4%BA%A4%E5%90%88%E5%B9%B6%E8%AF%B7%E6%B1%82%E3%80%82&amp;continue%5Bto%5D=javascript%3A%3B&amp;namespace_key=117364">编辑</button><button name="button" type="submit" class="btn btn-primary ide-edit-button ml-2 gl-mr-3 btn-inverted js-edit-blob-link-fork-toggler" data-action="edit" data-fork-path="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/forks?continue%5Bnotice%5D=%E6%82%A8%E4%B8%8D%E8%83%BD%E7%9B%B4%E6%8E%A5%E5%AF%B9%E6%AD%A4%E9%A1%B9%E7%9B%AE%E8%BF%9B%E8%A1%8C%E6%9B%B4%E6%94%B9%E3%80%82%E6%AD%A4%E9%A1%B9%E7%9B%AE%E7%9A%84Fork%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E5%88%9B%E5%BB%BA%EF%BC%8C%E6%82%A8%E5%8F%AF%E4%BB%A5%E5%9C%A8Fork%E9%A1%B9%E7%9B%AE%E4%B8%AD%E8%BF%9B%E8%A1%8C%E6%9B%B4%E6%94%B9%EF%BC%8C%E4%BB%A5%E4%BE%BF%E6%8F%90%E4%BA%A4%E5%90%88%E5%B9%B6%E8%AF%B7%E6%B1%82%E3%80%82&amp;continue%5Bnotice_now%5D=%E6%82%A8%E4%B8%8D%E8%83%BD%E7%9B%B4%E6%8E%A5%E5%AF%B9%E6%AD%A4%E9%A1%B9%E7%9B%AE%E8%BF%9B%E8%A1%8C%E6%9B%B4%E6%94%B9%E3%80%82%E6%AD%A4%E9%A1%B9%E7%9B%AE%E7%9A%84Fork%E9%A1%B9%E7%9B%AE%E6%AD%A3%E5%9C%A8%E5%88%9B%E5%BB%BA%EF%BC%8C%E6%82%A8%E5%8F%AF%E4%BB%A5%E5%9C%A8Fork%E9%A1%B9%E7%9B%AE%E4%B8%AD%E8%BF%9B%E8%A1%8C%E6%9B%B4%E6%94%B9%EF%BC%8C%E4%BB%A5%E4%BE%BF%E6%8F%90%E4%BA%A4%E5%90%88%E5%B9%B6%E8%AF%B7%E6%B1%82%E3%80%82&amp;continue%5Bto%5D=%2F-%2Fide%2Fproject%2Fqq_36758461%2Ffaster-rcnn-pytorch%2Fedit%2Fmaster%2F-%2Fvideo.py&amp;namespace_key=117364">Web IDE</button><div class="btn-group ml-2" role="group">

<button name="button" type="submit" class="btn btn-default js-edit-blob-link-fork-toggler" data-action="replace" data-fork-path="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/forks?continue%5Bnotice%5D=%E6%82%A8%E4%B8%8D%E8%83%BD%E7%9B%B4%E6%8E%A5%E5%AF%B9%E6%AD%A4%E9%A1%B9%E7%9B%AE%E8%BF%9B%E8%A1%8C%E6%9B%B4%E6%94%B9%E3%80%82%E6%AD%A4%E9%A1%B9%E7%9B%AE%E7%9A%84Fork%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E5%88%9B%E5%BB%BA%EF%BC%8C%E6%82%A8%E5%8F%AF%E4%BB%A5%E5%9C%A8Fork%E9%A1%B9%E7%9B%AE%E4%B8%AD%E8%BF%9B%E8%A1%8C%E6%9B%B4%E6%94%B9%EF%BC%8C%E4%BB%A5%E4%BE%BF%E6%8F%90%E4%BA%A4%E5%90%88%E5%B9%B6%E8%AF%B7%E6%B1%82%E3%80%82%E5%86%8D%E6%AC%A1%E5%B0%9D%E8%AF%95replace%E6%AD%A4%E6%96%87%E4%BB%B6%E3%80%82&amp;continue%5Bnotice_now%5D=%E6%82%A8%E4%B8%8D%E8%83%BD%E7%9B%B4%E6%8E%A5%E5%AF%B9%E6%AD%A4%E9%A1%B9%E7%9B%AE%E8%BF%9B%E8%A1%8C%E6%9B%B4%E6%94%B9%E3%80%82%E6%AD%A4%E9%A1%B9%E7%9B%AE%E7%9A%84Fork%E9%A1%B9%E7%9B%AE%E6%AD%A3%E5%9C%A8%E5%88%9B%E5%BB%BA%EF%BC%8C%E6%82%A8%E5%8F%AF%E4%BB%A5%E5%9C%A8Fork%E9%A1%B9%E7%9B%AE%E4%B8%AD%E8%BF%9B%E8%A1%8C%E6%9B%B4%E6%94%B9%EF%BC%8C%E4%BB%A5%E4%BE%BF%E6%8F%90%E4%BA%A4%E5%90%88%E5%B9%B6%E8%AF%B7%E6%B1%82%E3%80%82&amp;continue%5Bto%5D=%2Fmirrors%2Fbubbliiiing%2Ffaster-rcnn-pytorch%2F-%2Fblob%2Fmaster%2Fvideo.py&amp;namespace_key=117364">替换</button>
<button name="button" type="submit" class="btn btn-default js-edit-blob-link-fork-toggler" data-action="delete" data-fork-path="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/forks?continue%5Bnotice%5D=%E6%82%A8%E4%B8%8D%E8%83%BD%E7%9B%B4%E6%8E%A5%E5%AF%B9%E6%AD%A4%E9%A1%B9%E7%9B%AE%E8%BF%9B%E8%A1%8C%E6%9B%B4%E6%94%B9%E3%80%82%E6%AD%A4%E9%A1%B9%E7%9B%AE%E7%9A%84Fork%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E5%88%9B%E5%BB%BA%EF%BC%8C%E6%82%A8%E5%8F%AF%E4%BB%A5%E5%9C%A8Fork%E9%A1%B9%E7%9B%AE%E4%B8%AD%E8%BF%9B%E8%A1%8C%E6%9B%B4%E6%94%B9%EF%BC%8C%E4%BB%A5%E4%BE%BF%E6%8F%90%E4%BA%A4%E5%90%88%E5%B9%B6%E8%AF%B7%E6%B1%82%E3%80%82%E5%86%8D%E6%AC%A1%E5%B0%9D%E8%AF%95delete%E6%AD%A4%E6%96%87%E4%BB%B6%E3%80%82&amp;continue%5Bnotice_now%5D=%E6%82%A8%E4%B8%8D%E8%83%BD%E7%9B%B4%E6%8E%A5%E5%AF%B9%E6%AD%A4%E9%A1%B9%E7%9B%AE%E8%BF%9B%E8%A1%8C%E6%9B%B4%E6%94%B9%E3%80%82%E6%AD%A4%E9%A1%B9%E7%9B%AE%E7%9A%84Fork%E9%A1%B9%E7%9B%AE%E6%AD%A3%E5%9C%A8%E5%88%9B%E5%BB%BA%EF%BC%8C%E6%82%A8%E5%8F%AF%E4%BB%A5%E5%9C%A8Fork%E9%A1%B9%E7%9B%AE%E4%B8%AD%E8%BF%9B%E8%A1%8C%E6%9B%B4%E6%94%B9%EF%BC%8C%E4%BB%A5%E4%BE%BF%E6%8F%90%E4%BA%A4%E5%90%88%E5%B9%B6%E8%AF%B7%E6%B1%82%E3%80%82&amp;continue%5Bto%5D=%2Fmirrors%2Fbubbliiiing%2Ffaster-rcnn-pytorch%2F-%2Fblob%2Fmaster%2Fvideo.py&amp;namespace_key=117364">删除</button>
</div><div class="btn-group ml-2" role="group">
<button class="btn btn btn-sm js-copy-blob-source-btn" data-toggle="tooltip" data-placement="bottom" data-container="body" data-class="btn btn-sm js-copy-blob-source-btn" data-title="复制文件内容" data-clipboard-target=".blob-content[data-blob-id=&#39;1f01f25f93b0249ffc5bd86907f9874b76979bee&#39;] &gt; pre" type="button" title="复制文件内容" aria-label="复制文件内容"><svg class="s16" data-testid="copy-to-clipboard-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#copy-to-clipboard"></use></svg></button>
<a class="btn btn-sm has-tooltip" target="_blank" rel="noopener noreferrer" aria-label="打开原始文件" title="打开原始文件" data-container="body" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/raw/master/video.py"><svg class="s16" data-testid="doc-code-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#doc-code"></use></svg></a>
<a download="video.py" class="btn btn-sm has-tooltip" target="_blank" rel="noopener noreferrer" aria-label="下载" title="下载" data-container="body" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/raw/master/video.py?inline=false"><svg class="s16" data-testid="download-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#download"></use></svg></a>

</div></div>
</div>
<div class="js-file-fork-suggestion-section file-fork-suggestion hidden">
<span class="file-fork-suggestion-note">
您没有权限
<span class="js-file-fork-suggestion-section-action">
edit
</span>
files in this project directly. Please fork this project,
make your changes there, and submit a merge request.
</span>
<a class="js-fork-suggestion-button gl-button btn btn-grouped btn-inverted btn-success" rel="nofollow" data-method="post" href="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/blob/master/video.py">Fork</a>
<button class="js-cancel-fork-suggestion-button gl-button btn btn-grouped" type="button">
Cancel
</button>
</div>



<div class="blob-viewer" data-path="video.py" data-type="simple" data-url="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/blob/master/video.py?format=json&amp;viewer=simple">
<div class="text-center gl-mt-4 gl-mb-3">
<span class="gl-spinner gl-spinner-orange gl-spinner-md qa-spinner" aria-label="加载中"></span>
</div>

</div>


</article>
</div>

<div class="modal" id="modal-upload-blob">
<div class="modal-dialog modal-lg">
<div class="modal-content">
<div class="modal-header">
<h3 class="page-title">Replace video.py</h3>
<button aria-label="关闭" class="close" data-dismiss="modal" type="button">
<span aria-hidden>&times;</span>
</button>
</div>
<div class="modal-body">
<form class="js-quick-submit js-upload-blob-form" data-method="put" action="/mirrors/bubbliiiing/faster-rcnn-pytorch/-/update/master/video.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="AcKCf9bixIPZuK/s/7mvToywUxS5DCBkkgs/bed/VXT4yLn6jnWWEMWB6TwnqAC3INsaFsduDUnpqHs6rkLANA==" /><div class="dropzone">
<div class="dropzone-previews blob-upload-dropzone-previews">
<p class="dz-message light">
拖放文件到此处或<a class="markdown-selector" href="#">点击上传</a>
</p>
</div>
</div>
<br>
<div class="dropzone-alerts gl-alert gl-alert-danger gl-mb-5 data" style="display:none"></div>
<div class="form-group row commit_message-group">
<label class="col-form-label col-sm-2" for="commit_message-3a89c75ea6e7db8f5f69d6448198da3c">提交信息
</label><div class="col-sm-10">
<div class="commit-message-container">
<div class="max-width-marker"></div>
<textarea name="commit_message" id="commit_message-3a89c75ea6e7db8f5f69d6448198da3c" class="form-control js-commit-message" placeholder="Replace video.py" required="required" rows="3">
Replace video.py</textarea>
</div>
</div>
</div>

<input type="hidden" name="branch_name" id="branch_name" />
<input type="hidden" name="create_merge_request" id="create_merge_request" value="1" />
<input type="hidden" name="original_branch" id="original_branch" value="master" class="js-original-branch" />

<div class="form-actions">
<button name="button" type="button" class="btn gl-button btn-success btn-upload-file" id="submit-all"><div class="spinner spinner-sm gl-mr-2 js-loading-icon hidden"></div>
Replace file
</button><a class="btn gl-button btn-cancel" data-dismiss="modal" href="#">取消</a>
<div class="inline gl-ml-3">
将在Fork(fork)项目中中创建一个新的分支, 并开启一个新的合并请求。
</div>

</div>
</form></div>
</div>
</div>
</div>

</div>


</div>
</div>
</div>
</div>
<footer class="csdn_footer">
<a href="https://codechina.blog.csdn.net/" target="_blank">博客</a>
<a href="https://codechina.csdn.net/codechina/help-docs/-/issues" target="_blank">反馈建议</a>
<a href="https://codechina.csdn.net/codechina/help-docs/-/wikis/home" target="_blank">使用手册</a>
<a href="https://codechina.csdn.net/about" target="_blank">关于CODE CHINA</a>
<a href="https://about.gitlab.com/releases/2020/12/22/gitlab-13-7-released/" target="_blank">Powered&nbsp;by&nbsp;GITLAB&nbsp;CE&nbsp;v13</a>
</footer>



<script nonce="LJ1GF0JLE5/YK+EOtU8Bdw==">
//<![CDATA[
if ('loading' in HTMLImageElement.prototype) {
  document.querySelectorAll('img.lazy').forEach(img => {
    img.loading = 'lazy';
    let imgUrl = img.dataset.src;
    // Only adding width + height for avatars for now
    if (imgUrl.indexOf('/avatar/') > -1 && imgUrl.indexOf('?') === -1) {
      const targetWidth = img.getAttribute('width') || img.width;
      imgUrl += `?width=${targetWidth}`;
    }
    img.src = imgUrl;
    img.removeAttribute('data-src');
    img.classList.remove('lazy');
    img.classList.add('js-lazy-loaded', 'qa-js-lazy-loaded');
  });
}

//]]>
</script>
<div aria-labelledby="custom-notifications-title" class="modal fade" id="modal-106312-4053-Project" role="dialog" tabindex="-1">
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<h4 class="modal-title" id="custom-notifications-title">
自定义通知事件
</h4>
<button aria-label="关闭" class="close" data-dismiss="modal" type="button">
<span aria-hidden>&times;</span>
</button>
</div>
<div class="modal-body">
<div class="container-fluid">
<form class="custom-notifications-form" id="edit_notification_setting_164320" action="/-/notification_settings/164320" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="patch" /><input type="hidden" name="authenticity_token" value="P2J8ocmfsdDPym4S6DqVFb2ACTvjyzfrwPVDboE+4ZvGaEckkQjjQ9PzKMIwKzrsEetAOZ2pGsa7Vgc5yAN02w==" /><input type="hidden" name="project_id" id="project_id" value="4053" />
<input type="hidden" name="hide_label" id="hide_label" value="true" />
<div class="row">
<div class="col-lg-4">
<h4 class="gl-mt-0">通知事件</h4>
<p>
自定义通知级别继承自参与级别。使用自定义通知级别，您会收到参与级别及选定事件的通知。想了解更多信息，请查看 <a target="_blank" href="/codechina/help-docs/-/wikis/docs/user/account/email-notify">通知邮件</a>.
</p>
</div>
<div class="col-lg-8">
<div class="form-group">
<div class="form-check gl-mt-0">
<input name="notification_setting[new_release]" type="hidden" value="0" /><input id="modal-106312-4053-Project_notification_setting[new_release]" class="js-custom-notification-event form-check-input" type="checkbox" value="1" name="notification_setting[new_release]" />
<label class="form-check-label" for="modal-106312-4053-Project_notification_setting[new_release]">
<strong>
新发布
<span class="spinner is-loading gl-vertical-align-middle gl-display-none"></span>
<svg class="s16 is-done gl-display-none gl-vertical-align-middle gl-text-green-600" data-testid="check-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#check"></use></svg>
</strong>
</label>
</div>
</div>
<div class="form-group">
<div class="form-check">
<input name="notification_setting[new_note]" type="hidden" value="0" /><input id="modal-106312-4053-Project_notification_setting[new_note]" class="js-custom-notification-event form-check-input" type="checkbox" value="1" name="notification_setting[new_note]" />
<label class="form-check-label" for="modal-106312-4053-Project_notification_setting[new_note]">
<strong>
新建评论
<span class="spinner is-loading gl-vertical-align-middle gl-display-none"></span>
<svg class="s16 is-done gl-display-none gl-vertical-align-middle gl-text-green-600" data-testid="check-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#check"></use></svg>
</strong>
</label>
</div>
</div>
<div class="form-group">
<div class="form-check">
<input name="notification_setting[new_issue]" type="hidden" value="0" /><input id="modal-106312-4053-Project_notification_setting[new_issue]" class="js-custom-notification-event form-check-input" type="checkbox" value="1" name="notification_setting[new_issue]" />
<label class="form-check-label" for="modal-106312-4053-Project_notification_setting[new_issue]">
<strong>
新建Issue
<span class="spinner is-loading gl-vertical-align-middle gl-display-none"></span>
<svg class="s16 is-done gl-display-none gl-vertical-align-middle gl-text-green-600" data-testid="check-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#check"></use></svg>
</strong>
</label>
</div>
</div>
<div class="form-group">
<div class="form-check">
<input name="notification_setting[reopen_issue]" type="hidden" value="0" /><input id="modal-106312-4053-Project_notification_setting[reopen_issue]" class="js-custom-notification-event form-check-input" type="checkbox" value="1" name="notification_setting[reopen_issue]" />
<label class="form-check-label" for="modal-106312-4053-Project_notification_setting[reopen_issue]">
<strong>
重启Issue
<span class="spinner is-loading gl-vertical-align-middle gl-display-none"></span>
<svg class="s16 is-done gl-display-none gl-vertical-align-middle gl-text-green-600" data-testid="check-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#check"></use></svg>
</strong>
</label>
</div>
</div>
<div class="form-group">
<div class="form-check">
<input name="notification_setting[close_issue]" type="hidden" value="0" /><input id="modal-106312-4053-Project_notification_setting[close_issue]" class="js-custom-notification-event form-check-input" type="checkbox" value="1" name="notification_setting[close_issue]" />
<label class="form-check-label" for="modal-106312-4053-Project_notification_setting[close_issue]">
<strong>
关闭issue
<span class="spinner is-loading gl-vertical-align-middle gl-display-none"></span>
<svg class="s16 is-done gl-display-none gl-vertical-align-middle gl-text-green-600" data-testid="check-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#check"></use></svg>
</strong>
</label>
</div>
</div>
<div class="form-group">
<div class="form-check">
<input name="notification_setting[reassign_issue]" type="hidden" value="0" /><input id="modal-106312-4053-Project_notification_setting[reassign_issue]" class="js-custom-notification-event form-check-input" type="checkbox" value="1" name="notification_setting[reassign_issue]" />
<label class="form-check-label" for="modal-106312-4053-Project_notification_setting[reassign_issue]">
<strong>
重新指派Issue
<span class="spinner is-loading gl-vertical-align-middle gl-display-none"></span>
<svg class="s16 is-done gl-display-none gl-vertical-align-middle gl-text-green-600" data-testid="check-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#check"></use></svg>
</strong>
</label>
</div>
</div>
<div class="form-group">
<div class="form-check">
<input name="notification_setting[issue_due]" type="hidden" value="0" /><input id="modal-106312-4053-Project_notification_setting[issue_due]" class="js-custom-notification-event form-check-input" type="checkbox" value="1" name="notification_setting[issue_due]" />
<label class="form-check-label" for="modal-106312-4053-Project_notification_setting[issue_due]">
<strong>
Issue due
<span class="spinner is-loading gl-vertical-align-middle gl-display-none"></span>
<svg class="s16 is-done gl-display-none gl-vertical-align-middle gl-text-green-600" data-testid="check-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#check"></use></svg>
</strong>
</label>
</div>
</div>
<div class="form-group">
<div class="form-check">
<input name="notification_setting[new_merge_request]" type="hidden" value="0" /><input id="modal-106312-4053-Project_notification_setting[new_merge_request]" class="js-custom-notification-event form-check-input" type="checkbox" value="1" name="notification_setting[new_merge_request]" />
<label class="form-check-label" for="modal-106312-4053-Project_notification_setting[new_merge_request]">
<strong>
新建合并请求
<span class="spinner is-loading gl-vertical-align-middle gl-display-none"></span>
<svg class="s16 is-done gl-display-none gl-vertical-align-middle gl-text-green-600" data-testid="check-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#check"></use></svg>
</strong>
</label>
</div>
</div>
<div class="form-group">
<div class="form-check">
<input name="notification_setting[push_to_merge_request]" type="hidden" value="0" /><input id="modal-106312-4053-Project_notification_setting[push_to_merge_request]" class="js-custom-notification-event form-check-input" type="checkbox" value="1" name="notification_setting[push_to_merge_request]" />
<label class="form-check-label" for="modal-106312-4053-Project_notification_setting[push_to_merge_request]">
<strong>
Push to merge request
<span class="spinner is-loading gl-vertical-align-middle gl-display-none"></span>
<svg class="s16 is-done gl-display-none gl-vertical-align-middle gl-text-green-600" data-testid="check-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#check"></use></svg>
</strong>
</label>
</div>
</div>
<div class="form-group">
<div class="form-check">
<input name="notification_setting[reopen_merge_request]" type="hidden" value="0" /><input id="modal-106312-4053-Project_notification_setting[reopen_merge_request]" class="js-custom-notification-event form-check-input" type="checkbox" value="1" name="notification_setting[reopen_merge_request]" />
<label class="form-check-label" for="modal-106312-4053-Project_notification_setting[reopen_merge_request]">
<strong>
Reopen merge request
<span class="spinner is-loading gl-vertical-align-middle gl-display-none"></span>
<svg class="s16 is-done gl-display-none gl-vertical-align-middle gl-text-green-600" data-testid="check-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#check"></use></svg>
</strong>
</label>
</div>
</div>
<div class="form-group">
<div class="form-check">
<input name="notification_setting[close_merge_request]" type="hidden" value="0" /><input id="modal-106312-4053-Project_notification_setting[close_merge_request]" class="js-custom-notification-event form-check-input" type="checkbox" value="1" name="notification_setting[close_merge_request]" />
<label class="form-check-label" for="modal-106312-4053-Project_notification_setting[close_merge_request]">
<strong>
关闭合并请求
<span class="spinner is-loading gl-vertical-align-middle gl-display-none"></span>
<svg class="s16 is-done gl-display-none gl-vertical-align-middle gl-text-green-600" data-testid="check-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#check"></use></svg>
</strong>
</label>
</div>
</div>
<div class="form-group">
<div class="form-check">
<input name="notification_setting[reassign_merge_request]" type="hidden" value="0" /><input id="modal-106312-4053-Project_notification_setting[reassign_merge_request]" class="js-custom-notification-event form-check-input" type="checkbox" value="1" name="notification_setting[reassign_merge_request]" />
<label class="form-check-label" for="modal-106312-4053-Project_notification_setting[reassign_merge_request]">
<strong>
重新指派合并请求
<span class="spinner is-loading gl-vertical-align-middle gl-display-none"></span>
<svg class="s16 is-done gl-display-none gl-vertical-align-middle gl-text-green-600" data-testid="check-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#check"></use></svg>
</strong>
</label>
</div>
</div>
<div class="form-group">
<div class="form-check">
<input name="notification_setting[change_reviewer_merge_request]" type="hidden" value="0" /><input id="modal-106312-4053-Project_notification_setting[change_reviewer_merge_request]" class="js-custom-notification-event form-check-input" type="checkbox" value="1" name="notification_setting[change_reviewer_merge_request]" />
<label class="form-check-label" for="modal-106312-4053-Project_notification_setting[change_reviewer_merge_request]">
<strong>
Change reviewer merge request
<span class="spinner is-loading gl-vertical-align-middle gl-display-none"></span>
<svg class="s16 is-done gl-display-none gl-vertical-align-middle gl-text-green-600" data-testid="check-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#check"></use></svg>
</strong>
</label>
</div>
</div>
<div class="form-group">
<div class="form-check">
<input name="notification_setting[merge_merge_request]" type="hidden" value="0" /><input id="modal-106312-4053-Project_notification_setting[merge_merge_request]" class="js-custom-notification-event form-check-input" type="checkbox" value="1" name="notification_setting[merge_merge_request]" />
<label class="form-check-label" for="modal-106312-4053-Project_notification_setting[merge_merge_request]">
<strong>
合并请求被合并
<span class="spinner is-loading gl-vertical-align-middle gl-display-none"></span>
<svg class="s16 is-done gl-display-none gl-vertical-align-middle gl-text-green-600" data-testid="check-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#check"></use></svg>
</strong>
</label>
</div>
</div>
<div class="form-group">
<div class="form-check">
<input name="notification_setting[failed_pipeline]" type="hidden" value="0" /><input id="modal-106312-4053-Project_notification_setting[failed_pipeline]" class="js-custom-notification-event form-check-input" type="checkbox" value="1" checked="checked" name="notification_setting[failed_pipeline]" />
<label class="form-check-label" for="modal-106312-4053-Project_notification_setting[failed_pipeline]">
<strong>
流水线失败
<span class="spinner is-loading gl-vertical-align-middle gl-display-none"></span>
<svg class="s16 is-done gl-display-none gl-vertical-align-middle gl-text-green-600" data-testid="check-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#check"></use></svg>
</strong>
</label>
</div>
</div>
<div class="form-group">
<div class="form-check">
<input name="notification_setting[fixed_pipeline]" type="hidden" value="0" /><input id="modal-106312-4053-Project_notification_setting[fixed_pipeline]" class="js-custom-notification-event form-check-input" type="checkbox" value="1" checked="checked" name="notification_setting[fixed_pipeline]" />
<label class="form-check-label" for="modal-106312-4053-Project_notification_setting[fixed_pipeline]">
<strong>
修复的流水线
<span class="spinner is-loading gl-vertical-align-middle gl-display-none"></span>
<svg class="s16 is-done gl-display-none gl-vertical-align-middle gl-text-green-600" data-testid="check-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#check"></use></svg>
</strong>
</label>
</div>
</div>
<div class="form-group">
<div class="form-check">
<input name="notification_setting[success_pipeline]" type="hidden" value="0" /><input id="modal-106312-4053-Project_notification_setting[success_pipeline]" class="js-custom-notification-event form-check-input" type="checkbox" value="1" name="notification_setting[success_pipeline]" />
<label class="form-check-label" for="modal-106312-4053-Project_notification_setting[success_pipeline]">
<strong>
流水线成功完成
<span class="spinner is-loading gl-vertical-align-middle gl-display-none"></span>
<svg class="s16 is-done gl-display-none gl-vertical-align-middle gl-text-green-600" data-testid="check-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#check"></use></svg>
</strong>
</label>
</div>
</div>
<div class="form-group">
<div class="form-check">
<input name="notification_setting[moved_project]" type="hidden" value="0" /><input id="modal-106312-4053-Project_notification_setting[moved_project]" class="js-custom-notification-event form-check-input" type="checkbox" value="1" checked="checked" name="notification_setting[moved_project]" />
<label class="form-check-label" for="modal-106312-4053-Project_notification_setting[moved_project]">
<strong>
Moved project
<span class="spinner is-loading gl-vertical-align-middle gl-display-none"></span>
<svg class="s16 is-done gl-display-none gl-vertical-align-middle gl-text-green-600" data-testid="check-icon"><use xlink:href="/assets/icons-15cbe21ccc2237b075efb0b0d170fc8d6716882dbe4fefad34c18b914dbcf811.svg#check"></use></svg>
</strong>
</label>
</div>
</div>
</div>
</div>
</form></div>
</div>
</div>
</div>
</div>


</body>
</html>

