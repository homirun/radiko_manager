<template id="timeTable-template">
    <div id="time-table">
        <span v-once>{{ getTimeTable() }}</span>
        {{ timetableColumns }}
    </div>
</template>
<style>

</style>
<script>
    import axios from "axios";
    export default {
        data:function () {
            return{
                timetableColumns: [],
                timetableRows: [],
            }
        },
        methods:{
            getTimeTable: function(){
                let areaId = "JP13";
                const request = axios.create({
                    baseURL: "http://localhost:8000/api/timetables",
                    headers: {
                        "ContentType": "application/json",
                        "X-Requested-With": "XMLHttpRequest",
                    },
                    responseType: "json"
                });

                let res = "";
                request.get("/program/today?area_id=" + areaId).then((response) => {
                        this.parseResponse(response);
                        this.$emit('close');
                }).catch((error) => {
                        console.log(error);
                        //TODO: エラーメッセージ出す
                });

            },
            parseResponse: function(res){

                // stationName
                for (let i in res.data.radiko.stations.station) {
                    this.timetableColumns.push(res.data.radiko.stations.station[i].name);
                }

            }

        },
    }

</script>