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
          <td>{{ item[0] }}</td>
          <td>{{ item[1] }}</td>
          <td>{{ item[2] }}</td>
          <td>{{ item[3] }}</td>
          <td>{{ item[4] }}</td>
          <td>{{ item[5] }}</td>
          <td>{{ item[6] }}</td>
          <td>{{ item[7] }}</td>
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