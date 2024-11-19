// Lms

// استيراد الثيم الافتراضي من VuePress 🖌️
import { defaultTheme } from "@vuepress/theme-default";

// استيراد دالة تعريف إعدادات المستخدم في VuePress 🛠️
import { defineUserConfig } from "vuepress/cli";

// استيراد الباني Vite لاستخدامه مع VuePress ⚡
import { viteBundler } from "@vuepress/bundler-vite";

// تعريف قائمة جانبية للصفحة الرئيسية 🏠
const homeSidebar = [{ text: "Home", link: "/" }];

// تعريف قائمة جانبية لمحتوى Django 🐍
const djangoSidebar = [
  // Main Page
  { text: "Django", link: "/Learn_Django/index.md" },
  // Models
  {
    text: "Models",
    link: "/Learn_Django/models.md"
  },
  // Api
  {
    text: "Api",
    link: "/Learn_Django/api.md"
  }
];

// تصدير إعدادات المستخدم الرئيسية 📄
export default defineUserConfig({
  // لغة الموقع 🌐
  lang: "en-US",

  // عنوان الموقع الرئيسي 📚
  title: "LMS",

  // وصف الموقع 💬
  description: "My first VuePress Site",

  // إعدادات الثيم الافتراضي مع تخصيص بعض الخصائص 🛠️
  theme: defaultTheme({
    logo: "https://vuejs.press/images/hero.png",

    // شريط التنقل في الموقع 🚀
    navbar: ["/", "/Learn_Django/index", "/get-started"],

    // القوائم الجانبية المحددة لكل مسار 📂
    sidebar: {
      "/Learn_Django/index/": djangoSidebar
    }
  }),
  // استخدام الباني Vite لبناء المشروع ⚡
  bundler: viteBundler()
});
