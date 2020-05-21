<template>
  <div class="about">
    <h1>This is an about page</h1>
    <p>Random number from SERVER: {{ randomNumber }}</p>
    <button @click="getRandom">New random number</button>
    
    <p>DataSource from SERVER: {{ dataSource }}</p>
    <button @click="getDataSource">Get DataSource</button>
    <button @click="postDataSource">Post DataSource</button>
    <button @click="deleteDataSource">Delete DataSource</button>
  </div>
</template>

<script>
import axios from "axios"
//import qs from "query-string"
/*
//定制axios
const myaxios = axiosLib.create({
  paramsSerializer: params => qs.stringify(params),
});
const getData = ({ data }) => data;
myaxios.interceptors.response.use(getData);
*/

//举例restful
const DataSource = {
  get: ({ id }) => axios.get(`api/data_sources/${id}`),
  post: data => axios.post(`api/data_sources/${data.id}`, data),
  delete: ({ id }) => axios.delete(`api/data_sources/${id}`),
};

export default {
  name: 'About',
  props: {
  },
  
  data () {
    return {
      randomNumber: 0,
      dataSource: '',
    }
  },
  
  methods: {
    getRandom () {
      this.randomNumber = this.getRandomLocal(1, 100)
      //this.randomNumber = this.getRandomFromServer()
    },
    getRandomLocal (min, max) {
      min = Math.ceil(min)
      max = Math.floor(max)
      return Math.floor(Math.random() * (max - min + 1)) + min
    },
    getRandomFromServer () {
      const path = '/api/random'
      axios.get(path)
        .then(response => {
          //console.log(response.data);
          this.randomNumber = response.data.random_number
        })
        .catch(error => {
          console.log(error);
        });
    },
    
    getDataSource () {
      DataSource.get({ id: this.getRandomLocal(1, 10000) }).then(response => {
        this.dataSource = response.data;
      });
    },
    
    postDataSource () {
      const newDataSource = {
        id:this.getRandomLocal(1, 10000),
        type:"mysql",
        ip:"192.168.1.1",
        port:3306,
      }
      DataSource.post(newDataSource).then(response => {
        this.dataSource = response.data;
      });
    },
    
    deleteDataSource () {
      DataSource.delete({ id: this.getRandomLocal(1, 10000) }).then(response => {
        this.dataSource = response.data;
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
