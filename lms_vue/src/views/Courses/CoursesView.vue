<template>
  <div class="courses">
    <div class="hero is-info">
      <div class="h-96 flex items-center justify-center bg-blue-400">
        <h1 class="title text-5xl font-bold text-white">Courses</h1>
      </div>
    </div>
    <section class="section">
      <div class="container mx-auto">
        <div class="grid_12 px-4 py-12">
          <!-- Courses [Categories] -->
          <div class="item_4">
            <aside class="menu">
              <p class="menu-label">Categories</p>

              <ul class="menu-list" v-if="categories.length">
                <li class="h-10 cursor-pointer p-2 border mb-2 mt-4 rounded-md">
                  <a :class="{ 'is-active': !activeCategory }" @click="setActiveCategory(null)">
                    All courses
                  </a>
                </li>
                <li
                  v-for="category in categories"
                  :key="category.id"
                  @click="setActiveCategory(category)"
                  class="h-10 cursor-pointer p-2 border mb-2 rounded-md"
                >
                  <a>{{ category.title }}</a>
                </li>
              </ul>

              <ul class="menu-list" v-else>
                <li>
                  <a class="h-6"> All courses </a>
                </li>
                <li>
                  <a>
                    <prime_skeleton
                      height="1.5rem"
                      width="10rem"
                      class="mt-2"
                      borderRadius="5px"
                    ></prime_skeleton>
                  </a>
                </li>
                <li>
                  <a>
                    <prime_skeleton
                      height="1.5rem"
                      width="10rem"
                      class="mt-2"
                      borderRadius="5px"
                    ></prime_skeleton>
                  </a>
                </li>
                <li>
                  <a>
                    <prime_skeleton
                      height="1.5rem"
                      width="10rem"
                      class="mt-2"
                      borderRadius="5px"
                    ></prime_skeleton>
                  </a>
                </li>
                <li>
                  <a>
                    <prime_skeleton
                      height="1.5rem"
                      width="10rem"
                      class="mt-2"
                      borderRadius="5px"
                    ></prime_skeleton>
                  </a>
                </li>
                <li>
                  <a>
                    <prime_skeleton
                      height="1.5rem"
                      width="10rem"
                      class="mt-2"
                      borderRadius="5px"
                    ></prime_skeleton>
                  </a>
                </li>
                <li>
                  <a>
                    <prime_skeleton
                      height="1.5rem"
                      width="10rem"
                      class="mt-2"
                      borderRadius="5px"
                    ></prime_skeleton>
                  </a>
                </li>
                <li>
                  <a>
                    <prime_skeleton
                      height="1.5rem"
                      width="10rem"
                      class="mt-2"
                      borderRadius="5px"
                    ></prime_skeleton>
                  </a>
                </li>
                <li>
                  <a>
                    <prime_skeleton
                      height="1.5rem"
                      width="10rem"
                      class="mt-2"
                      borderRadius="5px"
                    ></prime_skeleton>
                  </a>
                </li>
                <li>
                  <a>
                    <prime_skeleton
                      height="1.5rem"
                      width="10rem"
                      class="mt-2"
                      borderRadius="5px"
                    ></prime_skeleton>
                  </a>
                </li>
              </ul>
            </aside>
          </div>
          <!-- Courses [Course] -->
          <div class="item_8 p-4">
            <div class="grid_12 w-full" v-if="courses.length">
              <prime_card
                class="item_3 m-4"
                style="overflow: hidden"
                v-for="course in courses"
                v-bind:key="course.id"
              >
                <template #header>
                  <div class="h-80">
                    <img
                      v-if="course.get_image !== ''"
                      :src="course.get_image"
                      alt=""
                      class="w-full h-full"
                    />
                    <prime_skeleton v-else size="100%"></prime_skeleton>
                  </div>
                </template>
                <template #title>{{ course.title }}</template>
                <template #subtitle>Card subtitle</template>
                <template #content>
                  <p class="m-0">
                    {{ course.short_description }}
                  </p>
                </template>
                <template #footer>
                  <div class="flex gap-4 mt-1">
                    <!-- <router-link :to="{ name: 'Course', params: { slug: course.slug } }">
                        <prime_button label="More" severity="secondary" outlined class="w-full">
                        </prime_button>
                      </router-link> -->
                    <router-link :to="{ name: 'course', params: { id: course.id } }">
                      <prime_button label="More" severity="secondary" outlined class="w-full">
                      </prime_button>
                    </router-link>
                    <prime_button label="Save" class="w-full" />
                  </div>
                </template>
              </prime_card>
            </div>
            <div class="" v-else>
              <prime_card style="width: 25rem; overflow: hidden">
                <template #header>
                  <!-- <img
                      alt="user header"
                      src="https://primefaces.org/cdn/primevue/images/usercard.png"
                    /> -->
                  <prime_skeleton></prime_skeleton>
                </template>
                <template #title>Advanced Card</template>
                <template #subtitle>Card subtitle</template>
                <template #content>
                  <p class="m-0">
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed
                    consequuntur error repudiandae numquam deserunt quisquam repellat libero
                    asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate
                    neque quas!
                  </p>
                </template>
                <template #footer>
                  <div class="flex gap-4 mt-1">
                    <Button label="Cancel" severity="secondary" outlined class="w-full" />
                    <Button label="Save" class="w-full" />
                  </div>
                </template>
              </prime_card>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CoursesView',
  data() {
    return {
      courses: [],
      categories: [],
      activeCategory: null,
      loadingCourses: false,
      loadingCategories: false,
    }
  },
  components: {},
  async mounted() {
    document.title = 'Courses | Study Net'
    this.getCategory() // تحميل الأقسام
    this.getCourses() // تحميل الكورسات
  },
  methods: {
    setActiveCategory(category) {
      console.log(category)
      this.activeCategory = category
      // تحميل الكورسات بناءً على القسم النشط
      this.getCoursesByCategory()
    },
    getCourses() {
      axios.get('/api/courses/courses_list/').then((response) => {
        this.courses = response.data
      })
    },
    getCoursesByCategory() {
      this.loadingCourses = true
      let url = '/api/courses/courses_list_by_category/'
      if (this.activeCategory) {
        url += '?category_id=' + this.activeCategory.id
      }
      axios
        .get(url)
        .then((response) => {
          this.courses = response.data
          this.loadingCourses = false
        })
        .catch(() => {
          this.loadingCourses = false
        })
    },
    getCategory() {
      this.loadingCategories = true
      axios
        .get('/api/courses/categories_list/')
        .then((response) => {
          this.categories = response.data
          this.loadingCategories = false
        })
        .catch(() => {
          this.loadingCategories = false
        })
    },
  },
}
</script>
