<script setup></script>

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
        class="h-full"
      >
        <template #item="slotProps">
          <div class="border border-surface-200 dark:border-surface-700 rounded m-2 p-4">
            <div class="mb-4">
              <div class="relative mx-auto">
                <img :src="slotProps.data.imgUrl" alt="Name" class="w-full rounded" />
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
      </div>
    </div>
  </main>
</template>
<script>
import { ref } from 'vue'

export default {
  // for Carousel
  setup() {
    const products = ref([
      {
        imgUrl: '../assets/images/LMS_Learning_Management_System.png',
        name: 'Product Name 1',
        price: 20,
        inventoryStatus: 'INSTOCK',
      },
      {
        imgUrl: '../assets/images/LMS_Learning_Management_System_1.jpg',
        name: 'Product Name 2',
        price: 30,
        inventoryStatus: 'LOWSTOCK',
      },
    ])

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

    return { products, responsiveOptions, getSeverity }
  },
  data() {
    return {}
  },
  mounted() {},
  methods: {},
}
</script>
