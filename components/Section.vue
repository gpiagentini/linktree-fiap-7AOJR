<template>
    <span class="text-2xl font-bold text-center">
        {{ title }}
        <span class="cursor-pointer" @click="toggleText">
            <FontAwesomeIcon v-if="isTextVisible" :icon="faArrowAltCircleUp" />
            <FontAwesomeIcon v-if="!isTextVisible" :icon="faArrowAltCircleDown" />
        </span>
    </span>
    <p v-if="isTextVisible" class="text-center text-lg"> {{ text }} </p>
</template>

<script setup lang="ts">

import { defineProps } from 'vue'
import { faArrowAltCircleDown, faArrowAltCircleUp } from '@fortawesome/free-regular-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';


const { title, text } = defineProps(['title', 'text'])

const isTextVisible = ref(false)

const toggleText = () => {
    isTextVisible.value = !isTextVisible.value
}

</script>