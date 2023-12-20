<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const architect = ref({})
const architectError = ref()

const route = useRoute()

onMounted(async () => {
  try {
    const result = await axios.get(`http://localhost:3000/api/architects/${route.params.id}`)
    architect.value = result.data
  } catch (error) {
    architectError.value = error.message
    console.log('Error fetching data: ', error)
  }
})
</script>

<template>
  <div class="container px-5 py-12 mx-auto">
    <div class="grid lg:grid-cols-2 items-center" v-if="architect.name">
      <div class="relative">
        <img class="h-auto max-w-lg transition-all duration-300 rounded-lg shadow-lg filter"
             :src="architect.image" alt="architect image" />
      </div>
      <div>
        <h3 class="font-theme-heading text-2xl md:text-3xl font-medium text-center lg:text-left">{{ architect.name }}</h3>
        <p class="mt-4 font-theme-content text-lg text-theme-grayish-blue text-center lg:text-left" v-if="architect.bio.age">
          Age: {{ architect.bio.age }}
        </p>
        <p class="mt-4 font-theme-content text-lg text-theme-grayish-blue text-center lg:text-left" v-if="architect.bio.country">
          Place Of Birth: {{ architect.bio.country }}
        </p>
        <p class="mt-4 font-theme-content text-lg text-theme-dark-blue text-center lg:text-left" v-if="architect.bio.biography">
          {{ architect.bio.biography }}
        </p>
        <div class="grid lg:grid-cols-3 items-center">
        <div v-for="project in architect.projects" >
          <p  class="mt-4  font-theme-content text-xl text-theme-dark-blue text-center lg:text-left" >
            {{ project.name}}
          </p>
        </div>
        </div>

      </div>
    </div>
    <div v-else>
      <!-- Loading state or error message -->
      <p v-if="!architectError">Loading...</p>
      <p v-else>Error fetching data: {{ architectError }}</p>
    </div>
  </div>
</template>

