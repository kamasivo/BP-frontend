<template>
  <main role="main">
    <div class="card mt-3">
      <div class="card-header d-flex">
        <h5>List of vulnerabilities:</h5>
        <!-- <button class="btn btn-dark ml-auto" v-on:click="refresh">{{btnText}}</button> -->
      </div>
      <div class="card-body">
        <span>
          {{this.result}}
        </span>
      </div>
    </div>

  </main>
</template>


<script>
  export default {
    data () {
      return {
        devices: '',
        packets: '',
        ipAddresses: '',
        btnText: 'Refresh',
        result: ''
      }
    },
    created: async function(){
      this.loadVulnerabilites()
    },
    methods: {
      loadVulnerabilites: async function() {
        const res = await fetch("http://localhost:5000/api/vulns");
        const obj = await res.json();

        this.result = obj.data.data[0]

        // let array = obj.data.data;
        // this.result = Array.from( array.reduce((a,{ipAddressLocal, ...rest})=>{ 
        //   return a.set(ipAddressLocal, [rest].concat(a.get(ipAddressLocal)||[]));
        //   }, new Map())
        //   ).map(([ipAddressLocal, children])=>({ipAddressLocal,children}));
          // console.log(this.result)
      }
    }
  }
</script>


<style>
.bold {
  font-weight: bold;
}
</style>