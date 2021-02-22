<template>
  <main role="main">
    <div class="card mt-3">
      <div class="card-header">
        <h5>List of connected devices:</h5>
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
          <td>{{ item.ipAddress }}</td>
          <td>{{ item.os }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.vendor }}</td>
          <td>{{ item.osFamily }}</td>
          <td>{{ item.osGen }}</td>
          <td>{{ item.numOfVulns }}</td>
          <td>{{ item.openPorts }}</td>
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
        devices: 'aaa',
      }
    },
    created: async function(){
    const res = await fetch("http://localhost:5000/api/devices");
    const obj = await res.json();
    this.devices = obj.data;
    }
  }
</script>