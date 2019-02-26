<template id="modal-template">
    <transition name="modal">
        <div id="modal-wrap" v-on:click="$emit('close')">
            <div id="modal-container">
                <div id="modal-contents" v-on:click.stop>

                        <form action="http://localhost:8000/api/reserve/?format=api" @submit.prevent method="POST" enctype="application/x-www-form-urlencoded">
                            <input type="text" v-model="station_id" placeholder="stationId" name="station_id"><br>
                            <input type="date" v-model="start_date" placeholder="startDate" name="start_date"><br>
                            <input type="time" v-model="start_time" placeholder="startTime" name="start_time"><br>
                            <input type="text" v-model="rec_time" placeholder="recTime(min)" name="rec_time"><br>
                            <input type="text" v-model="title" placeholder="title" name="title"><br>
                            <!--<input type="text" name="numbering" placeholder="numbering">-->
                            <!--<div id="every_check"><input type="checkbox" name="every" value="True" checked="checked">毎週録音</div>-->
                            <!--<input type="submit" name="submit" value="登録">-->
                            <button v-on:click="sendReserve">submit</button>
                        </form>

                </div>
            </div>
        </div>
    </transition>
</template>
<script>
    import axios from "axios";
    import Vue from "vue";

    export default {
        data:function(){
            return {
                station_id: "",
                start_date: "",
                start_time: "",
                rec_time: "",
                title: "",
            }
        },
        methods: {
            sendReserve(){
                const request = axios.create({
                    baseURL: "http://localhost:8000/api",
                    headers: {
                        "Content-Type": "application/json",
                        "X-Requested-With": "XMLHttpRequest",
                    },
                    responseType: "json"
                });

                request.post(
                    "/reserve/",
                    JSON.stringify({
                        "station_id": this.station_id,
                        "start_date": this.start_date,
                        "start_time": this.start_time,
                        "rec_time": this.rec_time,
                        "title": this.title,
                    })
                ).then(function(response) {
                    console.log(response);
                    this.$emit('close');
                }).catch(function(error) {
                    console.log(error);
                    //TODO: エラーメッセージ出す
                });
            },
        }
    }

</script>
<style>

    #modal-wrap{
        background-color: rgba(0, 0, 0, .5);
        display: table;
        position: fixed;
        width: 100%;
        height: 100%;
        z-index: 999;
        top: 0;
    }
    #modal-container{
        display: table-cell;
        vertical-align: middle;
    }
    #modal-contents{
        background-color: #fff;
        width: 30vw;
        margin: 0 auto;
        padding: 20px;
        box-shadow:0 2px 10px 0 rgba(0, 0, 0, 0.72);
        border-radius: 10px;
        transition: all .3s ease;
    }
    .modal-leave-active{
        opacity: 0;
    }
    .modal-enter #modal-contents, .model-leave-active #modal-contents{
        transform: scale(0.8);
    }

    input[type="text"],input[type="submit"],input[type="date"],input[type="time"]{
        margin: 0;
        padding: 0;
        background: none;
        border: none;
        border-radius: 0;
        outline: none;
        -webkit-appearance: none;
        -moz-appearance: none;
        appearance: none;
    }
    input[type="text"],input[type="date"],input[type="time"]{
        border-bottom: solid 1px #bb8ab7;
        height: 2vh;
        width: 80%;
        font-size: 2vh;
        padding: 5px;
        margin: 20px auto;
        display: block;
    }

    button{
        border: solid 1px #bb8ab7;
        height: 4vh;
        width: 30%;
        padding: 5px;
        font-size: 1.5vh;
        color: #fff;
        background-color: #a563a0;
        margin: 20px auto;
        display: block;
        transition: 0.25s;
        box-shadow:0 2px 3px 0 rgba(0,0,0,0.5);
    }

    input[type="submit"]:hover {
        box-shadow: 0 4px 5px 0 rgba(0,0,0,0.5);
    }

    input[type="text"]:focus,input[type="date"]:focus,input[type="time"]:focus {
         border-bottom: solid 2px #bb8ab7;
    }
    #every_check{
        margin: 20px auto;
        font-size: 2vh;
        text-align: center;
    }
</style>