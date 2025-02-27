<template>
    <figure class="p-6">
        <img class="w-32 h-32 rounded-full mx-auto" :src="profile" alt="Profile" width="400" height="400" />
        <figcaption class="font-medium pt-6 text-center">
            <div class="text-cyan-900 text-xl">{{ title }}</div>
        </figcaption>
        <blockquote class="text-center space-y-4">
            <p class="text-lg font-medium">{{ quote }}</p>
        </blockquote>
    </figure>
</template>

<script setup lang="ts">

import { defineProps } from 'vue'

const { title, quote, profile } = defineProps(['title', 'quote', 'profile'])

</script>