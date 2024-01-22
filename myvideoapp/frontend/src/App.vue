<template>
	<main class="p-4 md:ml-64 h-auto pt-20">
		<RouterView />
	</main>
</template>

<script>
import axios from 'axios'
import { RouterLink, RouterView } from 'vue-router'

export default {
	setup() {
		return {
			RouterView,
			RouterLink
		}
	},
}
</script>
