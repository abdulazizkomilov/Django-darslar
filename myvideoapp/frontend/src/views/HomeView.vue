<!-- src/components/VideoList.vue -->

<template>
    <div>
        <h1>Video List</h1>
        <ul>
            <li v-for="video in videos" :key="video.id">
                <router-link :to="'/videos/' + video.id">{{ video.title }}</router-link>
            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios';
import { defineComponent } from 'vue';

export default defineComponent({
    data() {
        return {
            loading: true,
            videos: [],
        };
    },
    mounted() {
        this.getVideos();
    },
    methods: {
        getVideos() {
            axios
                .get('http://127.0.0.1:8000/api/videos/')
                .then(response => {
                    console.log(response.data);
                    this.videos = response.data;
                    this.loading = false;
                })
                .catch(error => {
                    console.error('Error fetching videos:', error);
                });
        },
    },
});
</script>
