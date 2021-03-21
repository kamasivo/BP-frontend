<template>
  <main role="main">
    <div class="card mt-3">
      <div class="card-header d-flex">
        <h5>List of connected devices:</h5>
        <button class="btn btn-dark ml-auto" v-on:click="refresh">{{btnText}}</button>
      </div>
      <div class="card-body">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">IP address</th>
              <th scope="col">Operation system</th>
              <th scope="col">Device name</th>
              <th scope="col">Vendor</th>
              <th scope="col">OS family</th>
              <th scope="col">OS gen</th>
              <th scope="col">Number of vulnerabilities</th>
              <th scope="col">Open ports</th>
            </tr>
          </thead>
          <tbody>
          <tr
          v-for="item in devices"
          :key="item.name"
          >
          <td>{{ item[0] }}</td>
          <td>{{ item[1] }}</td>
          <td>{{ item[2] }}</td>
          <td>{{ item[3] }}</td>
          <td>{{ item[5] }}</td>
          <td>{{ item[6] }}</td>
          <td>{{ item[4] }}</td>
          <td>{{ item[7] }}</td>
        </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="card mt-3">
      <div class="card-header d-flex">
        <h5>Types of transfered packets on the network</h5>
      </div>
      <div class="card-body">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">TCP</th>
              <th scope="col">UDP</th>
              <th scope="col">ICMP</th>
            </tr>
          </thead>
          <tbody>
          <td>{{this.packets.tcp}}</td>
          <td>{{this.packets.udp}}</td>
          <td>{{this.packets.icmp}}</td>
          </tbody>
        </table>
      </div>
    </div>

    <div class="card mt-3">
      <div class="card-header d-flex">
        <h5>List of connected devices:</h5>
        // eslint-disable-next-line vue/no-parsing-error
        {{this.ipAddresses}}
      </div>
      <div class="card-body">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">IP address</th>
              <th scope="col">Send packets</th>
            </tr>
          </thead>
          <tbody>
          <tr
          v-for="item in ipAddresses"
          :key="item.name"
          >
          <td>{{ item[0] }}</td>
          <td>{{ item[1] }}</td>
        </tr>
          </tbody>
        </table>
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
        btnText: 'Refresh'
      }
    },
    created: async function(){
    const res = await fetch("http://localhost:5000/api/devices");
    const obj = await res.json();
    this.devices = obj.data;

    const res2 = await fetch("http://localhost:5000/api/packets");
    const obj2 = await res2.json();
    this.packets = obj2.data;


    const res3 = await fetch("http://localhost:5000/api/ipAddresses");
    const obj3 = await res3.json();
    this.ipAddresses = obj3.data;
    console.log(this.devices)
    console.log(this.ipAddresses)
    },
    methods: {
      refresh: async function() {
        this.devices = ''
        this.btnText = 'Scanning the network ...'
        const res = await fetch("http://localhost:5000/api/refresh_devices");
        const obj = await res.json();
        this.devices = obj.data;
        this.btnText = 'Refresh'
      }
    }
  }
</script>