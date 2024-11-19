export const redirects = JSON.parse("{}")

export const routes = Object.fromEntries([
  ["/get-started.html", { loader: () => import(/* webpackChunkName: "get-started.html" */"F:/LMS_Learning_Management_System/lms_vuepress/docs/.vuepress/.temp/pages/get-started.html.js"), meta: {"title":"Get Started"} }],
  ["/", { loader: () => import(/* webpackChunkName: "index.html" */"F:/LMS_Learning_Management_System/lms_vuepress/docs/.vuepress/.temp/pages/index.html.js"), meta: {"title":"LMS Learning Management System"} }],
  ["/", { loader: () => import(/* webpackChunkName: "index.html" */"F:/LMS_Learning_Management_System/lms_vuepress/docs/.vuepress/.temp/pages/index.html.js"), meta: {"title":"Home"} }],
  ["/Learn_Django/api.html", { loader: () => import(/* webpackChunkName: "Learn_Django_api.html" */"F:/LMS_Learning_Management_System/lms_vuepress/docs/.vuepress/.temp/pages/Learn_Django/api.html.js"), meta: {"title":"تعلم Django"} }],
  ["/Learn_Django/", { loader: () => import(/* webpackChunkName: "Learn_Django_index.html" */"F:/LMS_Learning_Management_System/lms_vuepress/docs/.vuepress/.temp/pages/Learn_Django/index.html.js"), meta: {"title":"Learn Django"} }],
  ["/Learn_Django/models.html", { loader: () => import(/* webpackChunkName: "Learn_Django_models.html" */"F:/LMS_Learning_Management_System/lms_vuepress/docs/.vuepress/.temp/pages/Learn_Django/models.html.js"), meta: {"title":""} }],
  ["/404.html", { loader: () => import(/* webpackChunkName: "404.html" */"F:/LMS_Learning_Management_System/lms_vuepress/docs/.vuepress/.temp/pages/404.html.js"), meta: {"title":""} }],
]);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept()
  if (__VUE_HMR_RUNTIME__.updateRoutes) {
    __VUE_HMR_RUNTIME__.updateRoutes(routes)
  }
  if (__VUE_HMR_RUNTIME__.updateRedirects) {
    __VUE_HMR_RUNTIME__.updateRedirects(redirects)
  }
}

if (import.meta.hot) {
  import.meta.hot.accept(({ routes, redirects }) => {
    __VUE_HMR_RUNTIME__.updateRoutes(routes)
    __VUE_HMR_RUNTIME__.updateRedirects(redirects)
  })
}
