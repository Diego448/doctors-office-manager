<script lang="ts">
    import { defineComponent } from 'vue'

    export default defineComponent({

        props: [
            "patient", "mode"
        ],
        data() {
            return {
                data: {
                    "name": "",
                    "email": "",
                    "telephone_number": "",
                    "_id": ""
                },
                id: this.patient._id.$oid,
                lastStatusMessage: ""
            }
        },
        methods: {
            seutpMode() {
                if (this.mode === "add") {
                    this.data = {
                        "name": "",
                        "email": "",
                        "telephone_number": "",
                        "_id": ""
                    }
                } else {
                    this.data = this.patient;
                }
            },
            validateData() {
                let validatedData = (({name, email, telephone_number}) => ({name, email, telephone_number}))(this.data);
                return validatedData;
            },
            async save() {
                const response = await fetch("http://127.0.0.1:8000/patient/update/" + this.id, {
                    method: 'PATCH',
                    mode: 'cors',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(this.validateData())
                });
                return response.json();
            }
        },
        mounted() {
            this.seutpMode();
        },
        created() {},
        computed: {}
    })
</script>

<template>
    <div class="card-footer">
        <div class="row g-3 align-items-end">
            <div class="col-6">
                <label for="name">Patient name</label>
                <input type="text" id="name" required class="form-control" placeholder="Patient name" v-model="data.name"/>         
            </div>
            <div class="col-6">
                <label for="email">e-mail</label>
                <input type="email" id="email" v-model="data.email" class="form-control" placeholder="e-mail">    
            </div>
            <div class="col-3">
                <label for="TelephoneNumber">Telephone number</label>
                <input type="tel" id="TelephoneNumber" placeholder="Telephone number" required v-model="data.telephone_number" class="form-control"/>
            </div>
            <div class="col-auto">
                <input type="button" value="Save" class="btn btn-primary" @click="save"/>
            </div>
        </div>  
    </div>
</template>

<style>

</style>
