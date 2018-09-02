<template id="timeTable-template">
    <div id="time-table">
        {{ getTimeTable() }}
        {{ timetable }}
    </div>
</template>
<style>

</style>
<script>
    import axios from "axios";
    export default {
        data:function () {
            return{
                timetable:'',
            }
        },
        methods:{
            getTimeTable(){
                console.log("aaaa");
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
                        res = response.data.radiko.stations.station[0].name;
                        console.log(res);
                        this.timetable = res;
                        this.$emit('close');
                }).catch((error) => {
                        console.log(error);
                        //TODO: エラーメッセージ出す
                });

            }

        },
    }

</script>