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
    <div class="hero is-info px-4">
      <div class="hero-body has-text-centered">
        <h1 class="title">{{ course.title }}</h1>

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
          <div class="column item_2 border">
            <h2>Table of contents</h2>
            <ul v-if="lessons.length">
              <li v-for="lesson in lessons" v-bind:key="lesson.id">
                <a v-if="lesson">
                  <span @click="setActiveLesson(lesson)">{{ lesson.title }}</span>
                </a>
                <!-- <a>{{ lesson.title }}</a> -->
              </li>
            </ul>
            <ul v-else>
              <li>
                <a>Lesson 1</a>
              </li>
              <li>
                <a>Lesson 2</a>
              </li>
              <li>
                <a>Lesson 3</a>
              </li>
              <li>
                <a>Lesson 4</a>
              </li>
            </ul>
          </div>
          <div class="column item_10">
            <div class="">
              <template v-if="userStore.user.isAuthenticated">
                <template v-if="activeLesson">
                  <div class="">{{ activeLesson.title }}</div>
                  <div class="">{{ activeLesson.short_description }}</div>
                </template>
                <template v-else>
                  <div class="">Title</div>
                  <div class="">description</div>
                </template>
              </template>
              <template v-else>
                <h2>Restricted access</h2>
                <p>You need to have an account to continue!</p>
              </template>
            </div>
            <!--
            <template v-if="$store.state.user.isAuthenticated">
                <h2>{{ activeLesson.title }}</h2>

                <span class="tag is-warning" v-if="activity.status == 'started'" @click="markAsDone"
                  >Started (mark as done)</span
                >
                <span class="tag is-success" v-else>Done</span>

                <hr />

                {{ activeLesson.long_description }}

                <hr />

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
      </div>
    </section>
  </div>
</template>

<script>
// import axios from 'axios'

// import CourseComment from '@/components/CourseComment'
// import AddComment from '@/components/AddComment'
// import Quiz from '@/components/Quiz'
// import VideoOnYoutube from '@/components/Video'

export default {
  components: {
    // CourseComment,
    // AddComment,
    // Quiz,
    // VideoOnYoutube,
  },
  data() {
    return {
      course: {
        created_by: {
          id: 0,
        },
      },
      lessons: [],
      comments: [],
      activeLesson: null,
      errors: [],
      // quiz: {},
      activity: {},
    }
  },
  async mounted() {
    // console.log('mounted')
    this.getCourse()
    // const slug = this.$route.params.slug

    // await axios.get(`courses/${slug}/`).then((response) => {
    //   console.log(response.data)

    //   this.course = response.data.course
    //   this.lessons = response.data.lessons
    // })

    document.title = this.course.title + ' | StudyNet'
  },
  methods: {
    /*
        submitComment(comment) {
          this.comments.push(comment)
        },
        if (lesson.lesson_type === 'quiz') {
          this.getQuiz()
        } else {
          this.getComments()
        }
          this.trackStarted()
        trackStarted() {
          axios
            .post(`activities/track_started/${this.$route.params.slug}/${this.activeLesson.slug}/`)
            .then((response) => {
              console.log(response.data)
              this.activity = response.data
            })
        },
        markAsDone() {
          axios
            .post(`activities/mark_as_done/${this.$route.params.slug}/${this.activeLesson.slug}/`)
            .then((response) => {
              console.log(response.data)
              this.activity = response.data
            })
        },
        getQuiz() {
          axios
            .get(`courses/${this.course.slug}/${this.activeLesson.slug}/get-quiz/`)
            .then((response) => {
              console.log(response.data)
              this.quiz = response.data
            })
        },
        getComments() {
          axios
            .get(`courses/${this.course.slug}/${this.activeLesson.slug}/get-comments/`)
            .then((response) => {
              console.log(response.data)
              this.comments = response.data
            })
        },
    */
    getCourse() {
      axios.get(`/api/courses/course_detail/${this.$route.params.id}/`).then((response) => {
        let line = '📌'.repeat(30)
        console.log(` %c${line} `, 'color: #1cd07c; font-size: 16px')
        console.log('course response: ', response.data)
        console.log('course response: ', response.data.course)
        console.log('course lessons response: ', response.data.lessons)
        this.course = response.data.course
        this.lessons = response.data.lessons
      })
    },
    setActiveLesson(lesson) {
      this.activeLesson = lesson
    },
  },
}
</script>
