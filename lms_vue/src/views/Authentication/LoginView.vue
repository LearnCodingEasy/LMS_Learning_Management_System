<template>
  <div class="wrapper_page_login">
    <div class="inner_page_login">
      <div class="container mx-auto">
        <div class="wrapper_content_page_login flex justify-center items-center">
          <div class="inner_content_page_login">
            <!-- Signup -->
            <div class="mobile_body_dark">
              <span class="voice_up"> </span>
              <span class="voice_down"> </span>
              <span class="power"> </span>
              <span class="sonser"> </span>
              <span class="voice"> </span>
              <span class="carme"> </span>
              <div class="mobile_content">
                <form class="">
                  <prime_card class="prime_card_form_signup">
                    <template #header>
                      <div class="flex justify-between items-center w-full">
                        <div class="text font-bold text-5xl">Signup</div>
                        <div class="image_logo">
                          <img src="../../assets/Images/Messenger_80x80.png" class="" alt="" />
                        </div>
                      </div>
                    </template>
                    <template #content>
                      <prime_fluid class="prime_card_form_signup_content">
                        <div class="">
                          <div class="flex">
                            <!-- First name -->
                            <div class="mr-1">
                              <prime_input_text
                                placeholder="First name"
                                v-model="formSignup.name"
                              />
                            </div>
                            <!-- Surname -->
                            <div class="ml-1">
                              <prime_input_text
                                placeholder="Surname"
                                v-model="formSignup.surname"
                              />
                            </div>
                          </div>
                          <!-- Mobile number or email address -->
                          <div class="col-span-full">
                            <prime_input_text
                              placeholder="Mobile number or email address"
                              v-model="formSignup.email"
                            />
                          </div>
                          <!-- password1 -->
                          <div class="col-span-full">
                            <prime_input_password
                              placeholder="New Password"
                              v-model="formSignup.password1"
                            />
                          </div>
                          <!-- password2 -->
                          <div class="col-span-full">
                            <prime_input_password
                              placeholder="Repeat password"
                              v-model="formSignup.password2"
                            />
                          </div>
                          <!-- Date of birth -->
                          <div class="col-span-full">Date of birth</div>
                          <div class="col-span-full">
                            <div class="flex flex-col md:flex-row gap-2">
                              <!-- Day -->
                              <prime_input_group>
                                <prime_date_picker v-model="day" view="day" dateFormat="dd" />
                              </prime_input_group>
                              <!-- Month -->
                              <prime_input_group>
                                <prime_date_picker v-model="month" view="month" dateFormat="mm" />
                              </prime_input_group>
                              <!-- Year -->
                              <prime_input_group>
                                <prime_date_picker v-model="year" view="year" dateFormat="yy" />
                              </prime_input_group>
                            </div>
                          </div>
                          <!-- Gender -->
                          <div class="col-span-full">Gender</div>
                          <div class="flex flex-col md:flex-row gap-2">
                            <prime_input_group>
                              <prime_radio_button
                                v-model="formSignup.gender"
                                inputId="ingredient1"
                                name="gender"
                                value="Female"
                              />
                              <label for="ingredient1" class="ml-2"> Female </label>
                            </prime_input_group>
                            <prime_input_group>
                              <prime_radio_button
                                v-model="formSignup.gender"
                                inputId="ingredient2"
                                name="gender"
                                value="Male"
                              />
                              <label for="ingredient2" class="ml-2"> Male </label>
                            </prime_input_group>

                            <prime_input_group>
                              <prime_radio_button
                                v-model="formSignup.gender"
                                inputId="ingredient3"
                                name="gender"
                                value="Custom"
                              />
                              <label for="ingredient3" class="ml-2"> Custom </label>
                            </prime_input_group>
                          </div>
                        </div>
                      </prime_fluid>
                    </template>
                    <template #footer>
                      <div class="flex justify-center gap-2">
                        <button
                          type="submit"
                          class="d_block_important mt-1 mx-auto w_50 bg-green-500 py-3 px-5 rounded text-white"
                          @click.prevent="submitFormSignup"
                        >
                          Signup
                        </button>
                      </div>
                    </template>
                    <!-- Errors -->
                    <template v-if="errorsSignup.length > 0">
                      <prime_toast />
                    </template>
                  </prime_card>
                </form>
              </div>
            </div>
            <!-- Log in -->
            <div class="mobile_body_dark">
              <span class="voice_up"> </span>
              <span class="voice_down"> </span>
              <span class="power"> </span>
              <span class="sonser"> </span>
              <span class="voice"> </span>
              <span class="carme"> </span>
              <div class="mobile_content">
                <form class="">
                  <prime_card class="prime_card_form_login">
                    <template #header>
                      <div class="flex justify-between items-center w-full">
                        <div class="text font-bold text-5xl">Log in</div>
                        <div class="image_logo">
                          <img src="../../assets/Images/Messenger_80x80.png" class="" alt="" />
                        </div>
                      </div>
                    </template>
                    <template #content>
                      <!-- Mobile number or email address -->
                      <prime_fluid class="prime_card_form_signup_content">
                        <div class="input_email">
                          <div class="col-span-full">
                            <prime_input_text
                              placeholder="Mobile number or email address"
                              v-model="formLogin.email"
                            />
                          </div>
                        </div>
                      </prime_fluid>
                      <!-- password -->
                      <div class="input_password">
                        <prime_input_password
                          placeholder="Your Password"
                          v-model="formLogin.password"
                        />
                      </div>
                      <!-- is Online -->
                      <div class="input_check_box">
                        <label class="col-span-full">Is Online</label><br />
                        <input type="checkbox" v-model="setUserOnline.is_online" />
                        <label class="col-span-full">{{ setUserOnline.is_online }}</label>
                      </div>
                      <!--  -->
                      <div class="Forgotten_password">
                        <a href="#" class="text-blue-600 mx-auto my-2 block text-center"
                          >Forgotten password?</a
                        >
                        <hr />
                      </div>
                    </template>
                    <template #footer>
                      <div class="row">
                        <!-- Errors -->
                        <template v-if="errorsLogin.length > 0">
                          <prime_toast></prime_toast>
                        </template>
                        <!-- Login -->
                        <div class="mt-2">
                          <button
                            type="submit"
                            class="d_block_important mt-1 mb-2 mx-auto w_100 bg-red-500 py-3 px-5 rounded text-white"
                            @click.prevent="submitFormLogin"
                          >
                            Log In
                          </button>

                          <!-- Button Signup -->
                        </div>
                      </div>
                    </template>
                  </prime_card>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <prime_toast />
  </div>
</template>

<script>
import axios from 'axios'
// eslint-disable-next-line no-unused-vars
import { RouterLink } from 'vue-router'
import { useUserStore } from '@/stores/user'
export default {
  name: 'loginView',
  setup() {
    const userStore = useUserStore()
    return {
      userStore,
    }
  },
  data() {
    return {
      formLogin: {
        email: '',
        password: '',
      },
      errorsLogin: [],

      // Signup
      formSignup: {
        name: '',
        surname: '',
        email: '',
        date_of_birth: null,
        gender: '',
        password1: '',
        password2: '',
      },
      day: '',
      month: '',
      year: '',
      errorsSignup: [],
      setUserOnline: {
        is_online: true,
      },
    }
  },
  methods: {
    //
    submitFormSignup() {
      this.errorsSignup = []

      // استخراج اليوم، الشهر، والسنة من كائنات Date وتنسيقها
      const day = this.day.getDate().toString().padStart(2, '0')
      const month = (this.month.getMonth() + 1).toString().padStart(2, '0')
      const year = this.year.getFullYear()

      const formattedDate = `${year}-${month}-${day}`
      this.formSignup.date_of_birth = formattedDate

      if (this.formSignup.name === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User Name missing',
          detail: 'Your name is missing',
          life: 3000,
        })
        this.errorsSignup.push('Your name is missing')
      }
      if (this.formSignup.surname === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User Surname missing',
          detail: 'Your Surname is missing',
          life: 3000,
        })
        this.errorsSignup.push('Your surname is missing')
      }
      if (this.formSignup.email === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User Is missing',
          detail: 'Your e-mail is missing',
          life: 3000,
        })
        this.errorsSignup.push('Your e-mail is missing')
      }
      if (this.formSignup.password1 === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User passwordIs missing',
          detail: 'Your password is missing',
          life: 3000,
        })
        this.errorsSignup.push('Your password is missing')
      }
      if (this.formSignup.password1 !== this.formSignup.password2) {
        this.$toast.add({
          severity: 'error',
          summary: 'User  password does not match',
          detail: 'Your password  does not match',
          life: 3000,
        })
        this.errorsSignup.push('The password does not match')
      }
      if (this.errorsSignup.length === 0) {
        axios
          .post('/api/signup/', this.formSignup)
          .then((response) => {
            if (response.data.message === 'success') {
              if (response.data.email_sent) {
                this.$toast.add({
                  severity: 'success',
                  summary: 'User Registered',
                  detail: 'Please activate your account by clicking the link sent to your email.',
                  life: 3000,
                })
              }
              this.$toast.add({
                severity: 'success',
                summary: 'User Is Registered',
                detail: 'Please activate your account by clicking your email link',
                life: 3000,
              })
              this.formSignup.name = ''
              this.formSignup.surname = ''
              this.formSignup.email = ''
              this.formSignup.date_of_birth = ''
              this.formSignup.gender = ''
              this.formSignup.password1 = ''
              this.formSignup.password2 = ''
              // this.$router.push('/loginView')
              // window.location.reload()
            } else {
              const data = JSON.parse(response.data.message)
              this.$toast.add({
                severity: 'error',
                summary: 'Error Message',
                detail: 'Message Content Something went wrong. Please try again',
                life: 6000,
              })
              for (const key in data) {
                this.errors.push(data[key][0].message)
              }
              console.log(`Bad`, this.formSignup.date_of_birth)
              console.log(`Day`, this.day)
              console.log(`month`, this.month)
              console.log(`year`, this.year)
            }
          })
          .catch((error) => {
            console.log('error', error)
          })
      }
    },
    // Function Login
    async submitFormLogin() {
      this.errorsLogin = []
      if (this.formLogin.email === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User Name missing',
          detail: 'Your name is missing',
          life: 3000,
        })
        this.errorsLogin.push('Your e-mail is missing')
      }
      if (this.formLogin.password === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User password is missing',
          detail: 'Your password is missing',
          life: 3000,
        })
        this.errorsLogin.push('Your password is missing')
      }
      // Set Api Login
      if (this.errorsLogin.length === 0) {
        await axios
          .post('/api/login/', this.formLogin)
          .then((response) => {
            this.userStore.setToken(response.data)
            console.log('response.data: Set Api Login ', response.data)
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access
            setTimeout(() => {
              this.setUserIsOnline()
            }, 1000)
          })
          .catch((error) => {
            console.log('error', error)
            if (error.response.data.detail) {
              // Code If True
              this.$toast.add({
                severity: 'error',
                summary: 'Error Message',
                detail: `${error.response.data.detail}`,
                life: 6000,
              })
            }

            this.errorsLogin.push(
              'The email or password is incorrect! Or the user is not activated!',
            )
          })
      }
      // Get Api Me
      if (this.errorsLogin.length === 0) {
        await axios
          .get('/api/me/')
          .then((response) => {
            this.userStore.setUserInfo(response.data)
            this.$router.push('/')
          })

          .catch((error) => {
            console.log('error', error)
          })
      }
    },
    // 📝 Function Update Set User Is Online
    setUserIsOnline() {
      this.errorsFormInfo = []

      const userStore = useUserStore()
      if (this.errorsFormInfo.length === 0) {
        //   // التحقق من وجود بيانات المستخدم في المتجر
        if (userStore && userStore.user) {
          // console.log('userStore.user: ', userStore.user)
          //     // إعداد البيانات المرسلة مع الطلب
          let formData = new FormData()
          formData.append('is_online', this.setUserOnline.is_online)
          axios
            .post('/api/editprofile/', formData, {
              headers: {
                'Content-Type': 'multipart/form-data',
              },
            })
            .then((response) => {
              if (response.data.message === 'information updated') {
                // localStorage تحديث البيانات في
                // قم بتحديث معلومات المستخدم في المتجر
                // userStore.setUserInfo({
                //   id: userStore.user.id,
                //   name: userStore.user.name,
                //   surname: userStore.user.surname,
                //   email: userStore.user.email,
                //   date_of_birth: userStore.user.date_of_birth,
                //   gender: userStore.user.gender,
                //   get_avatar: userStore.user.get_avatar,
                //   get_cover: userStore.user.get_cover,
                //   is_online: response.data.user.is_online,
                // })
                this.$toast.add({
                  severity: 'success',
                  summary: `🧑 Profile`,
                  detail: `User Is Online `,
                  life: 3000,
                })
              }
            })
            .catch((error) => {
              console.log('error', error)
            })
        }
      }
    },
  },
  mounted() {
    document.title = 'Trello | Login'
  },
}
</script>

<!--
vscode@vscode.com
http://localhost:5173/profile/66cb0215-0daa-454e-be13-cd0853a14aa8

-->
