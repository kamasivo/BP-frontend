<template>
  <main role="main">

    <div class="card mt-3">
      <div class="card-header d-flex">
        <h5>Types of transfered packets on the network</h5>
        <button class="btn btn-dark ml-auto" v-on:click="refreshPackets">Refresh</button>
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
        <button class="btn btn-dark ml-auto" v-on:click="refreshIp">Refresh</button>
      </div>
      <div class="card-body">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">IP address</th>
              <th scope="col">Send packets</th>
              <th scope="col">Recieved packets</th>
              <th scope="col">Blacklisted</th>
            </tr>
          </thead>
          <tbody v-for="item in result" :key="item.index">
            <tr>
              <td colspan="4" class="bold">{{item.ipAddressLocal}}</td>
            </tr>
          <tr
            v-for="child in item.children" :key="child.index"
          >
            <td>{{ child.ipAddressForeign }}</td>
            <td>{{ child.sendPackets }}</td>
            <td>{{ child.receivedPackets }}</td>
            <td>{{ child.blackList }}</td>
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
        packets: '',
        ipAddresses: '',
        result: ''
      }
    },
    created: async function(){
      this.loadDevices()
      this.refreshPackets()
      this.refreshIp()
    },
    methods: {
      loadDevices: async function() {
        const res = await fetch("http://localhost:5000/api/devices");
        const obj = await res.json();
        this.devices = obj.data;
      },
      refreshPackets: async function() {
        const res = await fetch("http://localhost:5000/api/packets");
        const obj = await res.json();
        this.packets = obj.data;
      },
      refreshIp: async function() {
        const res = await fetch("http://localhost:5000/api/ipAddresses");
        const obj = await res.json();
        this.ipAddresses = obj.data;

        let array = obj.data.data;
        this.result = Array.from( array.reduce((a,{ipAddressLocal, ...rest})=>{ 
          return a.set(ipAddressLocal, [rest].concat(a.get(ipAddressLocal)||[]));
          }, new Map())
          ).map(([ipAddressLocal, children])=>({ipAddressLocal,children}));
      }
    }
  }
</script>


<style>
.bold {
  font-weight: bold;
}
</style>