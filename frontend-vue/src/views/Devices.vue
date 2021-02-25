<template>
  <main role="main">
    <!-- device item -->
    <div class="card mt-3" v-for="item in devices" :key="item[0]">
      <div class="card-header">
        <h5>{{item[2]}}</h5>
      </div>
      <div class="card-body">
        <span class="d-flex">
          <p class="font-weight-bold">IP address:</p>
          <p class="ml-2">{{item[0]}}</p>
        </span>
        <span class="d-flex">
          <p class="font-weight-bold">Open ports:</p>
          <p class="ml-2" v-if="ports[0][1] == item[0]">
            <span v-for="port in ports" :key="port[0]">
              {{port[0]}}, 
            </span>
          </p>
        </span>
        <span class="d-flex">
          <p class="font-weight-bold">Operation system:</p>
          <p class="ml-2">{{item[1]}}</p>
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
    <!-- device item END -->
  </main>
</template>

<script>
  export default {
    data () {
      return {
        devices: '',
        ports: [[]]
      }
    },
    created: async function(){
      const res = await fetch("http://localhost:5000/api/devices");
      const obj = await res.json();
      this.devices = obj.data;

      const res2 = await fetch("http://localhost:5000/api/devices_ports");
      const obj2 = await res2.json();
      this.ports = obj2.data;
      console.log(this.ports)
    },
  }
</script>



<style scoped>
.trashIcon {
  font-size: 20px;
}
</style>
