<template>
  <main role="main">
    <!-- device item -->
    <div class="card mt-3">
      <div class="card-header">
        <h5>DEVICE NAME</h5>
      </div>
      <div class="card-body">
        <span class="d-flex">
          <p class="font-weight-bold">IP address:</p>
          <p class="ml-2">192.168.1.10</p>
        </span>
        <span class="d-flex">
          <p class="font-weight-bold">Open ports:</p>
          <p class="ml-2">20, 30, 40, 50</p>
        </span>
        <span class="d-flex">
          <p class="font-weight-bold">Operation system:</p>
          <p class="ml-2">Windows 7</p>
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
            <!-- repeatable item -->
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
            <!-- repeatable item END -->
          </tbody>
        </table>
      </div>
    </div>
    <!-- device item END -->
  </main>
</template>

<style scoped>
.trashIcon {
  font-size: 20px;
}
</style>
