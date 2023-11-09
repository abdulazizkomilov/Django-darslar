<template>
    <section class="bg-white dark:bg-gray-900">
        <div class="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6 ">
            <div class="p-5">
                <form v-on:submit.prevent="submitForm" method="post">
                    <div class="mb-6">
                        <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Full Name</label>
                        <input v-model="name" type="text"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                            placeholder="Full Name" required>
                    </div>
                    <div class="mb-6">
                        <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                            Position
                        </label>
                        <input v-model="position" type="text" id="password"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                            required>
                    </div>
                    <div class="mb-6">
                        <label for="text" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                            Body
                        </label>
                        <input v-model="user_body" type="text" id="password"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                            required>
                    </div>
                    <button type="submit"
                        class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Submit</button>
                </form>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
import { useToastStore } from '@/stores/toast'

export default {
    name: 'FormView',

    setup() {
        const toastStore = useToastStore()

        return {
            toastStore
        }
    },

    data() {
        return {
            posts: [],
            name: '',
            position: '',
            user_body: '',
            errors: []
        }
    },

    methods: {
        submitForm() {
            console.log('submitForm', this.name, this.position, this.user_body)

            axios
                .post('/api/',
                    {
                        "full_name": this.name,
                        "position": this.position,
                        "info": this.user_body
                    }
                )
                .then(response => {
                    console.log('data', response.data)

                    this.posts.push(response.data)
                    this.name = ''
                    this.position = ''
                    this.user_body = ''
                    this.toastStore.showToast(5000, 'The post successfully created!', 'bg-blue')
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
    }
}
</script>
