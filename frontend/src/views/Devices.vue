<template>
  <main role="main">
      <div class="card-header d-flex mt-2">
        <h5 class="mb-0">List of devices</h5>
        <button class="btn btn-dark ml-auto" v-on:click="refresh">{{btnText}}</button>
      </div>
    <!-- device item -->
     <div class="card mt-3" v-for="item in result" :key="item[0]">
      <div class="card-header">
        <h5 class="font-weight-bold mt-2">{{item.ipAddress}}</h5>
      </div>
      <div class="card-body">
        <span class="d-flex flex-column">
          <div v-for="port in item.children" :key="port[1]" >
            <div class="d-flex mt-2">
              <span style="width: 120px;" class="font-weight-bold"> Port number: </span>
              <span> {{port.port}} </span>
            </div>  
            <div class="d-flex mt-2">
              <span style="width: 120px;" class="font-weight-bold"> State: </span>
              <span> {{port.state}} </span>
            </div> 
            <div class="d-flex mt-2">
              <span style="width: 120px;"  class="font-weight-bold"> Service name: </span>
              <span> {{port.name}} </span>
            </div>
             <div class="d-flex mt-2">
              <span style="width: 120px;"  class="font-weight-bold"> Product name: </span>
              <span> {{port.product}} </span>
            </div>
            <div class="d-flex mt-2">
              <span style="width: 120px;"  class="font-weight-bold"> Vulnerabilities: </span>
              <div class="d-flex flex-column">

              <div v-for="vuln in port.script" :key="vuln[1]" >
                <p class="mr-1"> {{vuln}} </p>
              </div>
              </div>
            </div>    
            <hr>          
          </div>
        </span>
      </div>
    </div> 
    <!-- device item END-->
  </main>
</template>

<script>
  export default {
    data () {
      return {
        btnText: 'Refresh',
        result: '',
      }
    },
    created: async function(){
      this.loadVulnerabilites()
    },
    methods: {
      loadVulnerabilites: async function() {
        const res = await fetch("http://localhost:5000/api/vulns");
        const obj = await res.json();
        this.handleData(obj)
      },
    refresh: async function() {
      this.result = ''
      this.btnText = 'Scanning the network for vulnerabilities ...'
      const res = await fetch("http://localhost:5000/api/refresh_vulns");
      const obj = await res.json();
      this.handleData(obj)
      this.btnText = 'Refresh'
    },
    handleData: function(obj) {
      let array = obj.data.data;
      this.result = Array.from( array.reduce((a,{ipAddress, ...rest})=>{ 
        return a.set(ipAddress, [rest].concat(a.get(ipAddress)||[]));
        }, new Map())
        ).map(([ipAddress, children])=>({ipAddress,children}));
        console.log(this.result)
      // first value is always null so shift
      this.result.shift()
      this.result.forEach(element => {
        element.children.shift()
          element.children.forEach(e => {
          e.script = e.script.split('\n');
        })
      }); 
    }
    }
  }
</script>
