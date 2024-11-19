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
                <li>
                  <a
                    v-bind:class="{ 'is-active': !activeCategory }"
                    @click="setActiveCategory(null)"
                  >
                    All courses
                  </a>
                </li>
                <li
                  v-for="category in categories"
                  v-bind:key="category.id"
                  @click="setActiveCategory(category)"
                >
                  <a>{{ category.title }}</a>
                </li>
              </ul>

              <ul class="menu-list" v-else>
                <li>
                  <a> All courses </a>
                </li>
                <li>
                  <a> Html </a>
                </li>
                <li>
                  <a> Css </a>
                </li>
                <li>
                  <a> Javascript </a>
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

// import CourseItem from '@/components/CourseItem.vue'

export default {
  name: 'CoursesView',
  data() {
    return {
      courses: [],
      categories: [],
      activeCategory: null,
    }
  },
  components: {
    // CourseItem,
  },
  async mounted() {
    document.title = 'Courses | Study Net'
    this.getCourses()
    this.getCategory()
  },
  methods: {
    setActiveCategory(category) {
      console.log(category)
      this.activeCategory = category

      this.getCourses()
    },
    getCourses() {
      // let url = 'courses/'

      // if (this.activeCategory) {
      //   url += '?category_id=' + this.activeCategory.id
      // }

      // axios.get(url).then((response) => {
      //   console.log(response.data)

      //   this.courses = response.data
      // })
      // console.log(`Yes`)
      axios.get('/api/courses/courses_list/').then((response) => {
        let line = '👉️'.repeat(30)
        console.log(` %c${line} `, 'color: #1cd07c; font-size: 16px')
        console.log('courses_list response: ', response)
        this.courses = response.data
        console.log('this.courses: ', this.courses)
        console.log('this.courses: ', this.courses.length)
      })
    },
    getCategory() {
      axios.get('/api/courses/categories_list/').then((response) => {
        let line = '📌'.repeat(30)
        console.log(` %c${line} `, 'color: #1cd07c; font-size: 16px')
        console.log('categories_list response: ', response)
        this.categories = response.data
      })
    },
  },
}
</script>
