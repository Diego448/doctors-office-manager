<script  lang="ts">

    import { defineComponent } from 'vue'

    export default defineComponent({

        props: {
            
        },
        data() {
            return {
                patients: null
            }
        },
        methods: {
            async getPatients() {
                this.patients = await (await fetch('http://127.0.0.1:8000/patient/all')).json()
            }
        },
        mounted() {

        },
        created() {
            this.getPatients()
        }
    })

</script>

<template>
  <main>
    <h1>Patients</h1>
    <li v-for="patient in patients">
    {{ patient.name }}
    </li>
  </main>
</template>