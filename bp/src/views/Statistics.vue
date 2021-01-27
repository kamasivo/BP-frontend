<template>
  <main role="main">
    <div class="card mt-3">
      <div class="card-header">
        <h5>List of connected devices:</h5>
      </div>
      <div class="card-body">
         <div>
    <b-table striped hover :items="items"></b-table>
  </div>
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

            <tr>
              <td scope="row">192.168.0.1</td>
              <td>TP-link</td>
              <td>xxxxxxxx</td>
              <td class="text-success">0</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </main>
</template>


<script>
  export default {
    data() {
      return {
        items: [
          { age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
          { age: 21, first_name: 'Larsen', last_name: 'Shaw' },
          { age: 89, first_name: 'Geneva', last_name: 'Wilson' },
          { age: 38, first_name: 'Jami', last_name: 'Carney' }
        ]
      }
    }
  }
</script>