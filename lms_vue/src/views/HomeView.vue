<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'

// تعريف البيانات المتغيرة
const products = ref([])
const responsiveOptions = ref([
  {
    breakpoint: '1400px',
    numVisible: 2,
    numScroll: 1,
  },
  {
    breakpoint: '1199px',
    numVisible: 3,
    numScroll: 1,
  },
  {
    breakpoint: '767px',
    numVisible: 2,
    numScroll: 1,
  },
  {
    breakpoint: '575px',
    numVisible: 1,
    numScroll: 1,
  },
])

// دالة لحساب مستوى المخزون
const getSeverity = (status) => {
  switch (status) {
    case 'INSTOCK':
      return 'success'
    case 'LOWSTOCK':
      return 'warn'
    case 'OUTOFSTOCK':
      return 'danger'
    default:
      return null
  }
}

// جلب البيانات من API عند تحميل المكون
const fetchCourses = async () => {
  try {
    const response = await axios.get('/api/courses/courses_list_frontpage/')
    products.value = response.data.map((course) => ({
      imgUrl: course.get_image,
      name: course.title,
      price: Math.floor(Math.random() * 100), // قيمة عشوائية للسعر
      inventoryStatus: 'INSTOCK', // افتراضياً مخزون متوفر
    }))
  } catch (error) {
    console.error('Error fetching courses:', error)
  }
}

// تنفيذ جلب البيانات
onMounted(fetchCourses)
</script>

<template>
  <main>
    <!-- Carousel -->
    <div class="card bg-blue-400 h-96">
      <prime_carousel
        :value="products"
        :numVisible="1"
        :numScroll="1"
        :responsiveOptions="responsiveOptions"
        circular
        :autoplayInterval="3000"
        class="h-96 w-full"
      >
        <template #item="slotProps">
          <div
            class="border border-surface-200 dark:border-surface-700 rounded m-2 p-4 h-80 w-full"
          >
            <div class="w-full h-full border">
              <div class="grid_12 h-80">
                <div class="item_3 mb-4 h-80">
                  <div class="relative mx-auto h-80 w-80">
                    <img :src="slotProps.data.imgUrl" alt="Name" class="w-full rounded h-full" />
                    <prime_tag
                      :value="slotProps.data.inventoryStatus"
                      :severity="getSeverity(slotProps.data.inventoryStatus)"
                      class="absolute"
                      style="left: 5px; top: 5px"
                    />
                  </div>
                </div>
                <div class="mb-4 font-medium">{{ slotProps.data.name }}</div>
                <div class="flex justify-between items-center">
                  <div class="mt-0 font-semibold text-xl">${{ slotProps.data.price }}</div>
                  <span>
                    <prime_button icon="pi pi-heart" severity="secondary" outlined />
                    <prime_button icon="pi pi-shopping-cart" class="ml-2" />
                  </span>
                </div>
              </div>
            </div>
          </div>
        </template>
      </prime_carousel>
    </div>
    <!-- Boxes -->
    <div class="wrapper_boxes my-6 py-6">
      <div class="container mx-auto">
        <div class="inner_boxes text-center p-4 grid xxlg_grid_3 xlg_grid_2 lg_grid_2 md_grid_1">
          <div class="box">
            <div class="icon_or_img">
              <span class="block">
                <i class="pi pi-home" style="font-size: 6rem"></i>
              </span>
            </div>
            <div class="title"><h2>Study From Your Home</h2></div>
            <div class="subtitle">
              <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit.</p>
            </div>
          </div>
          <div class="box">
            <div class="icon_or_img">
              <i class="pi pi-home" style="font-size: 6rem"></i>
            </div>
            <div class="title"><h2>Study From Your Home</h2></div>
            <div class="subtitle">
              <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit.</p>
            </div>
          </div>
          <div class="box">
            <div class="icon_or_img">
              <i class="pi pi-home" style="font-size: 6rem"></i>
            </div>
            <div class="title"><h2>Study From Your Home</h2></div>
            <div class="subtitle">
              <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit.</p>
            </div>
          </div>
        </div>
        <div class="link_started text-center my-6 py-8">
          <a href="" class="py-4 px-8 bg-blue-400 text-4xl text-white rounded">
            Click To Get Started
          </a>
        </div>
        <div class="grid_12">
          <prime_card
            class="item_3 m-4 shadow-md"
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
      </div>
    </div>
  </main>
</template>
<script>
export default {
  setup() {},
  data() {
    return {
      courses: [],
    }
  },
  mounted() {
    this.getCourses()
  },
  methods: {
    getCourses() {
      axios.get('/api/courses/courses_list_frontpage/').then((response) => {
        this.courses = response.data
      })
    },
  },
}
</script>
