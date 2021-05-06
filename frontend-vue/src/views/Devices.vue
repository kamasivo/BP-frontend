<template>
  <main role="main">
    <span>
      {{result}}
    </span>
    <!-- device item -->
     <div class="card mt-3" v-for="(item, index) in result" :key="item[0]">
      <div class="card-header">
        <h5 v-if="item[2]">{{item[2]}}</h5>
        <h5 v-else>Zariadenie {{index + 1}}</h5>
      </div>
      <div class="card-body">
        <span class="d-flex">
          <p class="font-weight-bold">IP address:</p>
          <p class="ml-1">{{item[1]}}</p>
        </span>
        <span class="d-flex">
          <p class="font-weight-bold mr-1">Open ports:</p>
          <p v-for="port in ports" :key="port[1]" >
            <span class="ml-1" v-if="port[1] == item[1]">
              {{port}}, 
            </span>
          </p>
        </span>
        <span class="d-flex">
          <p class="font-weight-bold">Operation system:</p>
          <p class="ml-2">{{item[2]}}</p>
        </span>
        <h5>Vulnerabilities:</h5>
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Description</th>
              <th scope="col">Link to solution</th>
              <th scope="col">Action</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td scope="row">1</td>
              <td>Short description</td>
              <td>Link</td>
              <td>
                <a href="#"> Ignore </a>
                <a class="ml-2" href="#">
                  <i class="fas fa-trash-alt text-danger trashIcon"></i>
                </a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div> 
    <!-- device item END-->
  </main>
</template>

<script>
  export default {
    data () {
      return {
        devices: '',
        ports: [[]],
        result: '',
      }
    },
    created: async function(){
//       const res = await fetch("http://localhost:5000/api/devices");
//       const obj = await res.json();
//       this.devices = obj.data;
//       console.log(this.devices)

//       const res2 = await fetch("http://localhost:5000/api/devices_ports");
//       const obj2 = await res2.json();
//       this.ports = obj2.data;
// console.log(this.ports)
      this.loadVulnerabilites()
    },
    methods: {
      loadVulnerabilites: async function() {
        const res = await fetch("http://localhost:5000/api/vulns");
        const obj = await res.json();

        this.result = obj.data.data

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



<style scoped>
.trashIcon {
  font-size: 20px;
}
</style>
