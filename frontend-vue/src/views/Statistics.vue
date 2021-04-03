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
        {{this.result}}
        <h5>List of connected devices:</h5>
        <button class="btn btn-dark ml-auto" v-on:click="refreshIp">Refresh</button>
      </div>
      <div class="card-body">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Local IP address</th>
              <th scope="col">Foreign IP address</th>
              <th scope="col">Send packets</th>
              <th scope="col">Recieved packets</th>
              <th scope="col">Blacklisted</th>
            </tr>
          </thead>
          <tbody>
          <tr
          v-for="item in ipAddresses.data"
          :key="item.index"
          >
          <td>{{ item.ipAddressLocal }}</td>
          <td>{{ item.ipAddressForeign }}</td>
          <td>{{ item.sendPackets }}</td>
          <td>{{ item.receivedPackets }}</td>
          <td>{{ item.blackList }}</td>
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
        btnText: 'Refresh',
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
      refresh: async function() {
        this.devices = ''
        this.btnText = 'Scanning the network ...'
        const res = await fetch("http://localhost:5000/api/refresh_devices");
        const obj = await res.json();
        this.devices = obj.data;
        this.btnText = 'Refresh'
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
        console.log(array)
        this.result = Array.from( array.reduce((a,{ipAddressLocal, ...rest})=>{ 
          return a.set(ipAddressLocal, [rest].concat(a.get(ipAddressLocal)||[]));
          }, new Map())
          ).map(([ipAddressLocal, children])=>({ipAddressLocal,children}));

          console.log(this.result)

          // todo..this is ready for nice table input...find table 
      }
    }
  }
</script>