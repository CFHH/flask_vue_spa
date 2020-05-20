<template>
  <div class="about">
    <h1>This is an about page</h1>
    <p>Random number from backend: {{ randomNumber }}</p>
    <button @click="getRandom">New random number</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'About',
  props: {
  },
  data () {
    return {
      randomNumber: 0
    }
  },
  methods: {
    getRandomInt (min, max) {
      min = Math.ceil(min)
      max = Math.floor(max)
      return Math.floor(Math.random() * (max - min + 1)) + min
    },
    getRandom () {
      //this.randomNumber = this.getRandomInt(1, 100)
      this.randomNumber = this.getRandomFromBackend()
    },
    getRandomFromBackend () {
      const path = '/api/random'
      axios.get(path)
        .then(response => {
          console.log(response.data);
          this.randomNumber = response.data.random_number
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  created () {
    this.getRandom()
  }
}
</script>

<style>
</style>
