<template id="timeTable-template">
    <div id="time-table">
        hogehogehoge
        {{ getTimeTable() }}
    </div>
</template>
<style>

</style>
<script>
    import axios from "axios";
    export default {
        data:{

        },
        methods: {

            getTimeTable(){
                console.log("aaaa");
                let areaId = "JP13";
                const request = axios.create({
                    baseURL: "http://radiko.jp/v2/api",
                    headers: {
                        "ContentType": "application/json",
                        "X-Requested-With": "XMLHttpRequest",
                    },
                    responseType: "json"
                });

                request.get("/program/today?area_id=" + areaId).then((response) => {
                        console.log(response);
                        this.$emit('close');
                }).catch((error) => {
                        console.log(error);
                        //TODO: エラーメッセージ出す
                });

            }
        },
    }

</script>