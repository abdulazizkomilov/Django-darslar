<template>
    <div>
        <h1>Video Detail</h1>
        <video controls width="600" height="400">
            <source :src="videoUrl" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
</template>


<script>
import axios from 'axios';

export default {
    data() {
        return {
            videoUrl: '',
        };
    },
    mounted() {
        this.getFeed();
    },
    methods: {
        getFeed() {
            const videoId = this.$route.params.id; // Doğru değeri aldığınızdan emin olun
            axios
                .get(`http://127.0.0.1:8000/api/videos/${videoId}/stream/`)
                .then(response => {
                    console.log('Video URL:', response.data);
                    this.videoUrl = response.data;
                })
                .catch(error => {
                    console.error('Video stream alınamadı:', error);
                })
        },
    }
};
</script>
