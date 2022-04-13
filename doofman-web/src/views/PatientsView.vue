<script  lang="ts">

import { defineComponent } from 'vue'
import PatientListItem from '../components/PatientListItem.vue'

export default defineComponent({
    props: {},
    data() {
        return {
            patients: null
        };
    },
    methods: {
        async getPatients() {
            this.patients = await (await fetch("http://127.0.0.1:8000/patient/all")).json();
        }
    },
    mounted() {},
    created() {
        this.getPatients();
    },
    components: { PatientListItem }
    })

</script>

<template>
  <main>
    <h1 class="h1 text-center">Patients</h1>
    <PatientListItem v-for="patient in patients" :patient="patient"/>
    <div class="d-grid gap-2 col-6 mx-auto">
        <button class="btn btn-primary" type="button">Add</button>
    </div>
  </main>
</template>