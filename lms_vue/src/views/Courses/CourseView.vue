<script setup>
// import { RouterLink, } from 'vue-router'
import axios from 'axios'

// import { ref } from 'vue'
//
import { onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'

const userStore = useUserStore()
userStore.initStore()
const router = useRouter()

onMounted(() => {
  // Perform any necessary operations on component mount
  if (!userStore.user.access) {
    // console.log('User Data: ', userStore.user.access)
    // Replace '/login' with your actual login route
    router.push('/login')
  } else {
    // Set default Authorization header for axios
    axios.defaults.headers.common['Authorization'] = `Bearer ${userStore.user.access}`
    // console.log('User Data: ', userStore.user)
  }
})
</script>

<template>
  <div class="courses">
    <div class="hero is-info">
      <div class="h-96 flex items-center justify-center bg-blue-400">
        <h1 class="title text-5xl font-bold text-white">{{ course.title }}</h1>
        <!-- <router-link
          :to="{ name: 'Author', params: { id: course.created_by.id } }"
          class="subtitle"
        >
          By {{ course.created_by.first_name + ' ' + course.created_by.last_name }}
        </router-link> -->
      </div>
    </div>
    <section class="section">
      <div class="container mx-auto">
        <div class="grid_12 content px-4">
          <!-- Course Control -->
          <div class="column item_2 border rounded-md p-2 mr-4">
            <h2>Table of contents</h2>
            <ul v-if="lessons.length">
              <li
                v-for="lesson in lessons"
                v-bind:key="lesson.id"
                class="h-8 my-2 border rounded-md px-2 cursor-pointer"
              >
                <a v-if="lesson">
                  <span @click="setActiveLesson(lesson)">{{ lesson.title }}</span>
                </a>
              </li>
            </ul>
            <ul v-else>
              <li>
                <a>
                  <prime_skeleton
                    height="2rem"
                    width="10rem"
                    class="mt-2"
                    borderRadius="8px"
                  ></prime_skeleton>
                </a>
              </li>
              <li>
                <a>
                  <prime_skeleton
                    height="2rem"
                    width="10rem"
                    class="mt-2"
                    borderRadius="8px"
                  ></prime_skeleton>
                </a>
              </li>
              <li>
                <a>
                  <prime_skeleton
                    height="2rem"
                    width="10rem"
                    class="mt-2"
                    borderRadius="8px"
                  ></prime_skeleton>
                </a>
              </li>
              <li>
                <a>
                  <prime_skeleton
                    height="2rem"
                    width="10rem"
                    class="mt-2"
                    borderRadius="8px"
                  ></prime_skeleton>
                </a>
              </li>
            </ul>
          </div>
          <!-- Lesson View -->
          <div class="column item_10">
            <div class="">
              <template v-if="userStore.user.isAuthenticated">
                <!-- If User Click To See Lesson -->
                <template v-if="activeLesson">
                  <div class="wrapper_lesson p-4">
                    <div class="inner_lesson">
                      <div class="title">
                        <h2 class="text-4xl font-bold">{{ activeLesson.title }}</h2>
                      </div>
                      <div class="short_description mt-4">
                        <p>{{ activeLesson.short_description }}</p>
                      </div>
                      <div class="long_description mt-2 mb-4">
                        <p>{{ activeLesson.long_description }}</p>
                      </div>
                      <!-- 🗨️ التعليقات -->
                      <div class="comments">
                        <h4>Comments</h4>
                        <div class="flex items-center">
                          <div v-if="comments.length" class="pt-4 w-full">
                            <div
                              class="grid_12 p-2 shadow-md w-full mt-4 rounded-md"
                              v-for="comment in comments"
                              :key="comment.id"
                            >
                              <div class="item_12 flex h-16 items-center">
                                <div class="get_image w-10 h-10">
                                  <img
                                    :src="comment.created_by.get_avatar"
                                    :alt="comment.created_by.name"
                                    class="rounded-full"
                                  />
                                </div>
                                <div class="pl-2">
                                  <p>
                                    <small class="uppercase font-bold">{{ comment.name }}</small> -
                                    {{ comment.created_at_formatted }} ago
                                  </p>
                                </div>
                              </div>
                              <div class="item_12 pl-2">
                                <p>
                                  {{ comment.content }}
                                </p>
                              </div>
                            </div>
                          </div>
                          <div v-else>
                            <p>No comments yet. Be the first to comment!</p>
                          </div>
                        </div>
                      </div>
                      <hr />
                      <!-- 📝 إضافة تعليق جديد -->
                      <div class="add_comment mt-4">
                        <form @submit.prevent="submitComment">
                          <prime_card class="shadow-md">
                            <template #header>
                              <h4 class="text-2xl font-bold py-4 px-4">Add a comment</h4>
                            </template>
                            <template #content>
                              <prime_fluid class="">
                                <div class="">
                                  <!-- First name -->
                                  <div class="mb-4">
                                    <prime_input_text
                                      placeholder="Full Name"
                                      v-model="comment.name"
                                    />
                                  </div>
                                  <!-- content -->
                                  <div class="mt-1">
                                    <prime_textarea
                                      placeholder="content"
                                      v-model="comment.content"
                                    />
                                  </div>
                                </div>
                              </prime_fluid>
                              <!-- <prime_button
                                class="button is-link mt-4"
                                @click.prevent="submitComment"
                                >Submit</prime_button
                              > -->
                              <prime_button
                                type="submit"
                                class="button is-link mt-4"
                                @click.prevent="submitComment"
                                >Submit</prime_button
                              >
                            </template>
                          </prime_card>
                        </form>
                      </div>
                    </div>
                  </div>
                </template>
                <template v-else>
                  <div class="p-4">
                    <div class="">
                      <prime_skeleton height="2rem"></prime_skeleton>
                      <prime_skeleton class="mt-2" height="10rem"></prime_skeleton>
                      <br />
                      <div class="flex items-center">
                        <prime_skeleton
                          shape="circle"
                          size="2rem"
                          class="mt-2 mr-2"
                        ></prime_skeleton>
                        <prime_skeleton width="10rem" class="mt-2"></prime_skeleton>
                      </div>
                      <prime_skeleton class="mt-2" height="4rem"></prime_skeleton>
                    </div>
                  </div>
                </template>
              </template>
              <template v-else>
                <h2>Restricted access</h2>
                <p>You need to have an account to continue!</p>
              </template>
            </div>
          </div>
          <!--

                <span class="tag is-warning" v-if="activity.status == 'started'" @click="markAsDone"
                  >Started (mark as done)</span
                >
                <span class="tag is-success" v-else>Done</span>



                <template v-if="activeLesson.lesson_type === 'quiz'">
                  <Quiz v-bind:quiz="quiz" />
                </template> -->

          <!-- <template v-if="activeLesson.lesson_type === 'video'">
                  <VideoOnYoutube v-bind:youtube_id="activeLesson.youtube_id" />
                </template> -->

          <!--
                <template v-if="activeLesson.lesson_type === 'article'">
                  <CourseComment
                    v-for="comment in comments"
                    v-bind:key="comment.id"
                    v-bind:comment="comment"
                  />

                  <AddComment
                    v-bind:course="course"
                    v-bind:activeLesson="activeLesson"
                    v-on:submitComment="submitComment"
                  />
                  </template>
                </template>

                <template v-else>
                  {{ course.long_description }}
                </template>
                </template>
            -->
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      course: {
        created_by: {
          id: 0,
        },
        title: '', // 🏷️ لإظهار عنوان الكورس في التايتل
      },
      lessons: [],
      comments: [], // 🗨️ قائمة التعليقات
      activeLesson: null, // 📝 الدرس النشط

      // For Add Comment
      comment: {
        name: '',
        content: '',
      },
      errorsAddComment: [],
      // quiz: {},
      activity: {},
    }
  },
  async mounted() {
    this.getCourse()
    this.getComments()
  },
  methods: {
    getCourse() {
      axios.get(`/api/courses/course_detail/${this.$route.params.id}/`).then((response) => {
        this.course = response.data.course
        this.lessons = response.data.lessons
        // 🏷️ تحديث العنوان بعد جلب البيانات
        document.title = this.course.title + ' | StudyNet'
      })
    },
    setActiveLesson(lesson) {
      this.activeLesson = lesson
      this.getComments() // 🗨️ جلب التعليقات عند تغيير الدرس النشط
    },
    async getComments() {
      if (!this.activeLesson) return
      await axios
        .get(
          `/api/courses/course_detail/${this.$route.params.id}/lesson/${this.activeLesson.id}/comments_list/`, // 🌐 استخدام المسار الجديد
        )
        .then((response) => {
          console.log(`comments`, response.data)
          this.comments = response.data // 🗨️ تحديث قائمة التعليقات
        })
    },
    async submitComment() {
      this.errorsAddComment = []
      if (this.comment.name === '') {
        this.errorsAddComment.push('The name must be filled out')
        this.$toast.add({
          severity: 'error',
          summary: `Error Add Comment`,
          detail: `The name must be filled out`,
          life: 3000,
        })
      }
      if (this.comment.content === '') {
        this.errorsAddComment.push('The content must be filled out')
        this.$toast.add({
          severity: 'error',
          summary: `Error Add Comment`,
          detail: `The content must be filled out`,
          life: 3000,
        })
      }
      if (!this.errorsAddComment.length) {
        if (!this.activeLesson) return
        console.log('this.activeLesson.id: ', this.activeLesson.id)
        await axios
          // 🌐 استخدام المسار الجديد
          .post(
            `/api/courses/course_detail/${this.$route.params.id}/lesson/${this.activeLesson.id}/add_comment/`,
            this.comment,
          )
          .then((response) => {
            console.log(`comments`, response.data)
            this.comment.name = ''
            this.comment.content = ''

            this.getComments() // جلب التعليقات المحدثة
          })
          .catch((error) => {
            console.log(error)
            console.log(`error`, error)
          })
      }
    },
  },
}
</script>
