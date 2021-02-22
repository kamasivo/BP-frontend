

<template>
  <main role="main">
   <p>{{ greeting }}</p>
    <p>{{ flaskGreeting }}</p>
  </main>
</template>


<script>
export default {
    name: 'App',
    components: {
        
    },
    data: function(){
        return {
            greeting: 'Hello, Vue!',
            flaskGreeting: ''
        }
    },
    created: async function(){
    const gResponse = await fetch("http://localhost:5000/api/greeting");
    const gObject = await gResponse.json();
    this.flaskGreeting = gObject.greeting;
    }
}
</script>

