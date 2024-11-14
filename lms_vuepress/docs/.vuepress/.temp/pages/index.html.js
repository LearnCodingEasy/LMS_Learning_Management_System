import comp from "F:/LMS_Learning_Management_System/lms_vuepress/docs/.vuepress/.temp/pages/index.html.vue"
const data = JSON.parse("{\"path\":\"/\",\"title\":\"LMS Learning Management System\",\"lang\":\"en-US\",\"frontmatter\":{},\"headers\":[{\"level\":2,\"title\":\"Github\",\"slug\":\"github\",\"link\":\"#github\",\"children\":[]},{\"level\":2,\"title\":\"LICENSE\",\"slug\":\"license\",\"link\":\"#license\",\"children\":[]},{\"level\":2,\"title\":\"Vite Press\",\"slug\":\"vite-press\",\"link\":\"#vite-press\",\"children\":[]}],\"git\":{},\"filePathRelative\":\"index.md\"}")
export { comp, data }

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept()
  if (__VUE_HMR_RUNTIME__.updatePageData) {
    __VUE_HMR_RUNTIME__.updatePageData(data)
  }
}

if (import.meta.hot) {
  import.meta.hot.accept(({ data }) => {
    __VUE_HMR_RUNTIME__.updatePageData(data)
  })
}
