<template>
  <!-- Features Section Start -->
  <div id="features" class="container mx-auto px-5">
    <section class="py-16">
      <div class="w-4/5 md:w-3/5 mx-auto">
        <h2 class="text-3xl md:text-4xl font-semibold font-theme-heading text-center">Most Notable</h2>
        <p class="text-theme-grayish-blue text-center mt-7 font-theme-content text-lg">Discover Architectural Icons &
          Visionaries: Unveiling the Greatest Works and Stories of Master Architects</p>
      </div>

      <div class="mt-10">
        <ul class="flex flex-col items-center md:flex-row justify-center font-theme-heading">
          <li v-for="architect in list_architects" :key="architect.id"
              :class="isOpen === architect.id ? 'md:border-b-4 md:border-theme-secondary' : ''"
              class="w-full md:w-56 cursor-pointer hover:text-theme-secondary transition duration-200 border-b-2 border-t-2 md:border-t-0 flex justify-center">
            <a @click.prevent="isOpen = architect.id" href="#"
               :class="isOpen === architect.id ? ' border-theme-secondary' : ''" class="py-5  md:border-b-0 border-b-4">
              {{ architect.name }}
            </a>
          </li>
        </ul>
      </div>

      <div class="mt-16">
        <!-- Tab Content -->
        <template v-for="architect in list_architects" :key="architect.id">
          <div v-show="isOpen === architect.id" class="grid  lg:grid-cols-2 items-center">
            <div class="relative">
              <img class=" h-auto max-w-lg transition-all duration-300 rounded-lg shadow-lg  filter"
                   :src="architect.image" alt="architect image" />
              <div
                class="-z-10 bg-theme-primary h-52 w-96 sm:h-80 sm:w-full rounded-r-full absolute -left-56 -bottom-16"></div>
            </div>
            <div>
              <h3 class="font-theme-heading text-2xl md:text-3xl font-medium text-center lg:text-left">{{ architect.name
                }}</h3>
              <p class="mt-4 font-theme-content text-lg text-theme-grayish-blue text-center lg:text-left">Age:
                {{ architect.bio.age }}</p>
              <p class="mt-4 font-theme-content text-lg text-theme-grayish-blue text-center lg:text-left">Place Of
                Birth: {{ architect.bio.country }}</p>
              <p class="mt-4 font-theme-content text-lg text-theme-dark-blue text-center lg:text-left">
                {{ architect.bio.biography }}</p>
              <div class="flex justify-center lg:justify-start mt-7">
                <LinkButton btn-type="primary" :link="architect.id">More Info</LinkButton>
              </div>
            </div>
          </div>
        </template>
        <!-- Tab Content -->
      </div>
    </section>
  </div>
  <!-- Features Section End -->
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'

const isOpen = ref(1)
const list_architects = ref([])

onMounted(async () => {
  try {
    const result = await axios.get('http://localhost:3000/api/')
    list_architects.value = result.data
  } catch (error) {
    console.error('Error fetching data', error)
  }
})
</script>

