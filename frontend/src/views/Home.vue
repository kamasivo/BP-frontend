<template>
  <main role="main">
    <div class="card mt-3">
      <div class="card-header d-flex">
        <h5>List of connected devices</h5>
        <button class="btn btn-dark ml-auto" v-on:click="refresh">{{btnText}}</button>
      </div>
      <div class="card-body">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">IP address</th>
              <th scope="col">Operation system</th>
              <!-- <th scope="col">Device name</th> -->
              <th scope="col">Vendor</th>
              <th scope="col">OS family</th>
              <th scope="col">OS gen</th>
              <th scope="col">Open ports</th>
            </tr>
          </thead>
          <tbody>
          <tr
          v-for="item in devices"
          :key="item.name"
          >
          <td>{{ item[1] }}</td>
          <td>{{ item[2] }}</td>
          <!-- <td>{{ item[3] }}</td> -->
          <td>{{ item[4] }}</td>
          <td>{{ item[6] }}</td>
          <td>{{ item[7] }}</td>
          <td>{{ item[8] }}</td>
        </tr>
          </tbody>
        </table>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  name: "Home",
  data () {
    return {
        devices: '',
        btnText: 'Refresh',
        result: ''
    }
  },
  created: async function(){
      this.loadDevices()
    },
  methods: {
    refresh: async function() {
      this.devices = ''
      this.btnText = 'Scanning the network ...'
      const res = await fetch("http://localhost:5000/api/refresh_devices");
      const obj = await res.json();
      this.devices = obj.data;
      this.btnText = 'Refresh'
    },
    loadDevices: async function() {
        const res = await fetch("http://localhost:5000/api/devices");
        const obj = await res.json();
        this.devices = obj.data;
      },
  }
};
</script>

<style scoped>

</style>
