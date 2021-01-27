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
            <!-- repeatable item -->
            <tr>
              <td scope="row">192.168.0.1</td>
              <td>TP-link</td>
              <td>xxxxxxxx</td>
              <td class="text-success">0</td>
            </tr>
            <!-- repeatable item END -->
            <!-- repeatable item -->
            <tr>
              <td scope="row">192.168.0.1</td>
              <td>TP-link</td>
              <td>xxxxxxxx</td>
              <td class="text-success">0</td>
            </tr>
            <!-- repeatable item END -->
            <!-- repeatable item -->
            <tr>
              <td scope="row">192.168.0.1</td>
              <td>TP-link</td>
              <td>xxxxxxxx</td>
              <td class="text-success">0</td>
            </tr>
            <!-- repeatable item END -->
          </tbody>
        </table>
      </div>
    </div>
  </main>
</template>

<style scoped></style>
