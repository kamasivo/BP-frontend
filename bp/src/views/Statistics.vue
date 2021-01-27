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
              <th scope="col">Device name</th>
              <th scope="col">Operation system</th>
              <th scope="col">Number of vulnerabilities</th>
            </tr>
          </thead>
          <tbody>
          <tr
          v-for="item in devices"
          :key="item.name"
          >
          <td>{{ item.ip }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.os }}</td>
          <td>{{ item.vulns }}</td>
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
        devices: [
          {
            ip: '192.168.10.1',
            name: 'Frozen Yogurt',
            os: 'Win 7',
            vulns: '1'
          },
            {
            ip: '192.168.10.1',
            name: 'Frozen Yogurt',
            os: 'Win 7',
            vulns: '1'
          },   {
            ip: '192.168.10.1',
            name: 'Frozen Yogurt',
            os: 'Win 7',
            vulns: '1'
          },
        ],
      }
    },
  }
</script>