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
    mounted() {
    },
    created() {
        this.getPatients();
    },
    components: { PatientListItem }
})

</script>

<template>
  <main>
    <h1>Patients</h1>
    <PatientListItem v-for="patient in patients" :patient="patient"/>
  </main>
</template>