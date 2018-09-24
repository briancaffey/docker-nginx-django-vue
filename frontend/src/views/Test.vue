<template>

    <div><p v-for="i in visits" :key="i">{{i}}</p></div>

</template>


<script>

export default {
  name: 'Test',
  data() {
    return {
      visits: [4, 5, 6],
    };
  },
  mounted() {
    this.fetchVists();
  },
  methods: {
    fetchVists() {
      fetch('/api/visits/', {
        method: 'GET',
        headers: {
          Accept: 'application/json',
        },
      }).then((response) => {
        if (response.ok) {
          response.json().then((json) => {
            console.log(json);
            this.visits = json.all;
          });
        }
      });
    },
  },
};

</script>
