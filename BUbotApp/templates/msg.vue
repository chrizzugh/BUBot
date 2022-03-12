<template class="font-nunito">
    <Navbar />

    <div class="desktopVersion min-h-screen">
        <div
            class="bg-gray-50 flex h-screen justify-center divide-x divide-light-gray-700 px-2"
        >
            <!--Inbox Corner-->
            <div
                class="mt-20 shadow-md vsv:w-full vsvs:w-full x-v:w-full se:w-full vvs:w-full lvs:w-full vs:w-full ssm:w-full xsm:w-full sm:w-full mt-20 md:w-2/5 w-1/4 relative"
            >
                <div
                    id="msgheader"
                    class="flex justify-items-center relative shadow pt-5 pb-1"
                >
                    <button
                        class="focus:outline-none pl-5 hover:text-red-700"
                        type="button"
                    >
                        <span class="material-icons pt-1" id="iMessage">
                            chat</span
                        >
                    </button>
                    <h4 class="tracking-wider text-base font-bold pl-4">
                        Message
                    </h4>
                </div>

                <div
                    v-if="searchMessageInactive"
                    class="flex justify-center w-full relative py-1 mt-2 pt-2"
                >
                    <input
                        type="text"
                        class="h-8 w-11/12 pl-5 border font-normal text-sm focus:outline-none focus:ring-1 focus:ring-gray-300 rounded-full"
                        placeholder="Search"
                    />
                    <button
                        @click="searchBtn"
                        class="align-middle absolute right-8 pt-1 h-7 focus:outline-none hover:text-red-700"
                    >
                        <span class="material-icons" style="font-size: 22px">
                            search
                        </span>
                    </button>
                </div>
                <!---end of search bar-->

                <button
                    v-if="showSearchResults"
                    class="flex justify-center w-full relative py-1 mt-2 pt-2 focus:outline-none"
                >
                    <input
                        type="text"
                        class="h-8 w-10/12 pl-5 border font-normal text-sm focus:outline-none focus:ring-1 focus:ring-gray-300 rounded-full"
                        placeholder="Mark"
                        id="search"
                    />
                    <button
                        class="align-middle mt-1 ml-1 flex items-center h-6 w-6 rounded-full bg-gray-300 focus:outline-none hover:text-red-700"
                    >
                        <span
                            @click="closeSearchResults"
                            class="material-icons pl-1"
                            style="font-size: 17px"
                        >
                            close
                        </span>
                    </button></button
                ><!---end of search bar-->

                <div
                    class="overflow-auto overflow-x-hidden px-0 py-1 h-4/5"
                    id="scrollInbox"
                >
                    <div v-if="searchMessageInactive">
                        <button
                            @click="active_convo('Mark Aral')"
                            type="button"
                            class="focus:bg-gray-200 relative w-full sm:pr-8 flex focus:outline-none justify-between items-center mt-2 p-2 hover:shadow-lg cursor-pointer transition"
                        >
                            <div class="flex ml-2">
                                <img
                                    src="https://ptetutorials.com/images/user-profile.png"
                                    alt="sunil"
                                    class="rounded-lg h-8 w-7 pt-1"
                                />
                                <div
                                    class="flex flex-col justify-between items-start ml-2"
                                >
                                    <span class="font-medium text-sm" id="mark">
                                        {{ inbox[0].name }}
                                        <span
                                            class="material-icons pl-2"
                                            id="iCheck"
                                            style="font-size: 14px"
                                        >
                                            check_circle
                                        </span></span
                                    >
                                    <span
                                        class="text-xs text-gray-400 truncate w-36 md:w-28 lvs:w-64 sm:w-64 ssm:w-24"
                                    >
                                        {{ inbox[0].message }}
                                    </span>
                                </div>
                            </div>
                            <div class="flex flex-col items-start">
                                <span class="text-gray-700 text-xs">
                                    <span class="font-bold pl-1 pr-1">·</span
                                    >{{ inbox[0].time }}</span
                                >
                            </div>
                        </button>

                        <button
                            @click="active_convo('Gwen Lopez')"
                            type="button"
                            class="focus:bg-gray-200 relative w-full sm:pr-8 flex focus:outline-none justify-between items-center mt-2 p-2 hover:shadow-lg cursor-pointer transition"
                        >
                            <div class="flex ml-2">
                                <img
                                    src="https://ptetutorials.com/images/user-profile.png"
                                    alt="sunil"
                                    class="rounded-lg h-8 w-7 pt-1"
                                />
                                <div
                                    class="flex flex-col justify-between items-start ml-2"
                                >
                                    <span class="font-medium text-sm" id="gwen"
                                        >{{ inbox[1].name
                                        }}<span
                                            class="material-icons pl-2"
                                            id="iCheck"
                                            style="font-size: 14px"
                                        >
                                            check_circle
                                        </span></span
                                    >
                                    <span
                                        class="text-xs text-gray-400 truncate w-32 md:w-28 lvs:w-64 sm:w-64 ssm:w-24"
                                    >
                                        {{ inbox[1].message }}
                                    </span>
                                </div>
                            </div>
                            <div class="flex flex-col items-start">
                                <span class="text-gray-700 text-xs">
                                    <span class="font-bold pl-1 pr-1">·</span
                                    >{{ inbox[1].time }}</span
                                >
                            </div>
                        </button>
                    </div>
                    <!---------------navigation message------------>

                    <div
                        v-if="showSearchResults"
                        class="divide-y divide-gray-300"
                    >
                        <div
                            class="py-2 flex justify-center font-normal text-xs italic"
                        >
                            <span>Search Results</span>
                        </div>
                        <div>
                            <button
                                @click="Void"
                                type="button"
                                class="focus:bg-gray-200 relative w-full flex sm:pr-8 focus:outline-none justify-between items-center mt-2 p-2 hover:shadow-lg cursor-pointer transition"
                            >
                                <div class="flex ml-2">
                                    <img
                                        src="https://ptetutorials.com/images/user-profile.png"
                                        alt="sunil"
                                        class="rounded-lg h-8 w-7 pt-1"
                                    />
                                    <div
                                        class="flex flex-col justify-between items-start ml-2"
                                    >
                                        <span
                                            class="font-medium text-sm italic"
                                            id="mark"
                                        >
                                            <span class="text-red-700"
                                                >Mark</span
                                            >
                                            Aral
                                            <span
                                                class="material-icons pl-2"
                                                id="iCheck"
                                            >
                                                check_circle
                                            </span></span
                                        >
                                        <span
                                            class="text-xs text-gray-400 truncate md:w-28 w-36 lvs:w-64 sm:w-72 ssm:w-24"
                                        >
                                            {{ inbox[0].message }}
                                        </span>
                                    </div>
                                </div>
                                <div class="flex flex-col items-start">
                                    <span class="text-gray-700 text-xs">
                                        <span class="font-bold pl-1 pr-1"
                                            >·</span
                                        >{{ inbox[0].time }}</span
                                    >
                                </div>
                            </button>
                        </div>
                    </div>
                    <!---------------search message results------------>
                </div>
            </div>
            <!--end of left corner-->

            <!------------------------------------------------------>

            <!---Chat Corner-->
            <div
                class="mt-20 shadow-md relative vsv:w-full vsvs:w-full x-v:w-full se:w-full vvs:w-full lvs:w-full vs:w-full ssm:w-full xsm:w-full sm:w-full mt-20 w-5/12 md:w-3/5"
            >
                <div
                    class="relative flex justify-items-center md:justify-items-center shadow py-3"
                >
                    <div class="flex flex-row justify-between">
                        <div class="flex flex-row">
                            <button
                                id="backNavigator"
                                class="focus:outline-none pl-5 hover:text-red-700"
                                @click="backChat"
                                type="button"
                            >
                                <span class="material-icons pt-2" id="iMessage">
                                    keyboard_backspace</span
                                >
                            </button>

                            <h4 class="text-base font-bold pt-2 pl-4">
                                {{ activeName }}
                            </h4>
                            <span class="material-icons pl-3 pt-3" id="iCheck">
                                check_circle
                            </span>
                        </div>

                        <div class="align-middle absolute right-2">
                            <button
                                @click="threedots"
                                class="focus:bg-gray-300 hover:bg-gray-300 rounded-full px-1 h-6 mr-3 focus:outline-none hover:text-red-700"
                                type="button"
                            >
                                <span class="material-icons"> more_horiz</span>
                            </button>
                        </div>
                    </div>
                </div>

                <div
                    class="overflow-auto overflow-x-hidden h-4/5"
                    id="journal-scroll"
                >
                    <div
                        v-if="ifHide"
                        class="sticky top-0 w-full p-3 flex justify items-center shadow-lg bg-white border"
                    >
                        <!-- sent offer 1--->
                        <div v-if="toggle1" class="text-sm w-full">
                            <div class="flex justify-between items-center">
                                <span
                                    >You sent an offer to
                                    <span class="font-semibold ml-2">{{
                                        recipient
                                    }}</span>
                                    <span class="ml-2">for</span>
                                    <span class="font-semibold ml-2"
                                        >Post {{ postNum }}
                                    </span></span
                                >

                                <button
                                    @click="vertiDots"
                                    class="w-4 h-6 py-1 pb-1 pr-1 rounded-full focus:outline-none hover:text-red-700 hover:bg-gray-300 active:bg-gray-300"
                                    type="button"
                                >
                                    <span
                                        class="material-icons"
                                        style="font-size: 17px"
                                    >
                                        more_verti</span
                                    >
                                </button>
                            </div>
                            <div class="flex justify-end pr-3">
                                <button
                                    @click="cancel_transact('offer')"
                                    class="mx-2 mt-2 h-7 px-2 hover:text-white hover:bg-gray-300 rounded-full border border-gray-700"
                                >
                                    <span>Cancel Offer</span>
                                </button>
                                <router-link
                                    to="/dashboard"
                                    class="flex items-center mx-2 mt-2 h-7 px-2 hover:bg-gray-300 rounded-full bg-red-700 text-white"
                                    ><span>View Post</span></router-link
                                >
                            </div>
                        </div>
                        <!------->

                        <!-- sent request 1--->
                        <div v-if="toggle2" class="text-sm w-full">
                            <div class="flex justify-between items-center">
                                <span
                                    >You sent a request to
                                    <span class="font-semibold ml-2">{{
                                        recipient
                                    }}</span>
                                    <span class="ml-2">for</span>
                                    <span class="font-semibold ml-2"
                                        >Post {{ postNum }}
                                    </span></span
                                >

                                <button
                                    @click="vertiDots"
                                    class="w-4 h-6 py-1 pb-1 pr-1 rounded-full focus:outline-none hover:text-red-700 hover:bg-gray-300 active:bg-gray-300"
                                    type="button"
                                >
                                    <span
                                        class="material-icons"
                                        style="font-size: 17px"
                                    >
                                        more_verti</span
                                    >
                                </button>
                            </div>
                            <div class="flex justify-end pr-3">
                                <button
                                    @click="cancel_transact('request')"
                                    class="mx-2 mt-2 h-7 px-2 hover:text-white hover:bg-gray-300 rounded-full border border-gray-700"
                                >
                                    <span>Cancel Request</span>
                                </button>
                                <router-link
                                    to="/dashboard"
                                    class="flex items-center mx-2 mt-2 h-7 px-2 hover:bg-gray-300 rounded-full bg-red-700 text-white"
                                    ><span>View Post</span></router-link
                                >
                            </div>
                        </div>
                        <!------->
                        <!-- received offer 1--->
                        <div v-if="toggle3" class="text-sm w-full">
                            <div class="flex justify-between items-center">
                                <span
                                    ><span class="font-semibold mr-2">{{
                                        sender
                                    }}</span
                                    >sent you an offer
                                    <span class="ml-2">for your </span>
                                    <span class="font-semibold ml-2"
                                        >Post {{ postNum2 }}
                                    </span></span
                                >
                                <button
                                    @click="vertiDots"
                                    class="w-4 h-6 py-1 pb-1 pr-1 rounded-full focus:outline-none hover:text-red-700 hover:bg-gray-300 active:bg-gray-300"
                                    type="button"
                                >
                                    <span
                                        class="material-icons"
                                        style="font-size: 17px"
                                    >
                                        more_verti</span
                                    >
                                </button>
                            </div>
                            <div class="flex justify-end pr-3">
                                <button
                                    @click="declineDisOffer('offer')"
                                    class="mx-2 mt-2 h-7 px-2 hover:text-white hover:bg-gray-300 focus:outline-none rounded-full border border-gray-700"
                                >
                                    <span>Decline</span>
                                </button>
                                <button
                                    @click="acceptDisOffer('offer')"
                                    class="mx-2 mt-2 h-7 px-2 hover:bg-gray-300 rounded-full focus:outline-none bg-red-700 text-white"
                                >
                                    <span>Accept</span>
                                </button>
                            </div>
                        </div>
                        <!------->
                        <!-- received request 1--->
                        <div v-if="toggle4" class="text-sm w-full">
                            <div class="flex justify-between items-center">
                                <span
                                    ><span class="font-semibold mr-2">{{
                                        sender
                                    }}</span
                                    >sent you a request
                                    <span class="ml-2">for your </span>
                                    <span class="font-semibold ml-2"
                                        >Post {{ postNum2 }}
                                    </span></span
                                >
                                <button
                                    @click="vertiDots"
                                    class="w-4 h-6 py-1 pb-1 pr-1 rounded-full focus:outline-none hover:text-red-700 hover:bg-gray-300 active:bg-gray-300"
                                    type="button"
                                >
                                    <span
                                        class="material-icons"
                                        style="font-size: 17px"
                                    >
                                        more_verti</span
                                    >
                                </button>
                            </div>
                            <div class="flex justify-end pr-3">
                                <button
                                    @click="declineDisOffer('request')"
                                    class="mx-2 mt-2 h-7 px-2 hover:text-white hover:bg-gray-300 focus:outline-none rounded-full border border-gray-700"
                                >
                                    <span>Decline</span>
                                </button>
                                <button
                                    @click="acceptDisOffer('request')"
                                    class="mx-2 mt-2 h-7 px-2 hover:bg-gray-300 rounded-full focus:outline-none bg-red-700 text-white"
                                >
                                    <span>Accept</span>
                                </button>
                            </div>
                        </div>
                        <!------->
                        <!--------------transaction details confirmed------>
                        <div v-if="toggle5" class="text-sm w-full">
                            <div class="flex flex-row justify-between">
                                <span
                                    >Transaction
                                    <span class="font-semibold ml-2"
                                        >{{ postNum2 }}
                                    </span>
                                </span>

                                <div class="flex items-center">
                                    <span
                                        class="rounded border h-6 border-blue-700 px-1"
                                        >Confirmed</span
                                    >

                                    <button
                                        @click="vertiDots"
                                        class="w-4 h-6 py-1 pb-1 pr-1 rounded-full focus:outline-none hover:text-red-700 hover:bg-gray-300 active:bg-gray-300"
                                        type="button"
                                    >
                                        <span
                                            class="material-icons"
                                            style="font-size: 17px"
                                        >
                                            more_verti</span
                                        >
                                    </button>
                                </div>
                            </div>
                            <div class="flex justify-end pr-3">
                                <button
                                    @click="toggleViewDetails"
                                    class="mx-2 mt-2 h-7 px-2 hover:text-white hover:bg-gray-300 focus:outline-none rounded-full border border-gray-700"
                                >
                                    <span>View Details</span>
                                </button>
                                <button
                                    @click="
                                        (toggle_status = !toggle_status),
                                            (trans_id = itemx.id)
                                    "
                                    class="mx-2 mt-2 h-7 px-2 hover:bg-gray-300 rounded-full focus:outline-none bg-red-700 text-white"
                                >
                                    <span>Update</span>
                                </button>
                            </div>
                        </div>
                        <!------------------->

                        <!--------------transaction details cancelled------>
                        <div v-if="toggle6" class="text-sm w-full">
                            <div class="flex flex-row justify-between">
                                <span
                                    >Transaction
                                    <span class="font-semibold ml-2"
                                        >{{ postNum2 }}
                                    </span>
                                </span>
                                <div class="flex items-center">
                                    <span
                                        class="rounded border h-6 border-crimsonRed text-crimsonRed px-1"
                                        >Cancelled</span
                                    >
                                    <button
                                        @click="vertiDots"
                                        class="w-4 h-6 py-1 pb-1 pr-1 rounded-full focus:outline-none hover:text-red-700 hover:bg-gray-300 active:bg-gray-300"
                                        type="button"
                                    >
                                        <span
                                            class="material-icons"
                                            style="font-size: 17px"
                                        >
                                            more_verti</span
                                        >
                                    </button>
                                </div>
                            </div>
                            <div class="flex justify-end pr-3">
                                <button
                                    @click="toggleViewDetails"
                                    class="mx-2 mt-2 h-7 px-2 hover:text-white hover:bg-gray-300 focus:outline-none rounded-full border border-gray-700"
                                >
                                    <span>View Details</span>
                                </button>
                                <button
                                    @click="VOID"
                                    class="bg-opacity-50 mx-2 mt-2 h-7 px-2 rounded-full focus:outline-none bg-red-700 text-white"
                                >
                                    <span>Update</span>
                                </button>
                            </div>
                        </div>
                        <!------------------->

                        <!-----vertical-dot  options-->
                        <div
                            v-if="toggleVerti"
                            id="vertiOPTIONS"
                            class="md:absolute md:right-4 md:top-2 fixed top-36 right-0 px-2 mr-4 bg-gray-200 w-2/5 shadow-inner rounded-lg border-solid border-2 border-white"
                            style="width: 220px"
                        >
                            <div class="flex flex-col">
                                <div class="flex flex-row items-center">
                                    <button
                                        @click="hideVertiOptions"
                                        class="w-full flex py-1 hover:bg-white hover:text-crimsonRed justify-start mt-2 border border-gray-300 rounded-lg items-center"
                                    >
                                        <span
                                            class="material-icons pl-3"
                                            style="font-size: 20px"
                                            >visibility</span
                                        >
                                        <span class="font-semibold pl-2"
                                            >Hide</span
                                        >
                                    </button>
                                </div>
                                <div class="divide-y divide-gray-300">
                                    <div class="flex flex-col pb-2">
                                        <span
                                            class="pl-1 font-semibold py-1 text-gray-500 py-1 text-xs tracking-wide"
                                            >Request(s)/Offers RECEIVED</span
                                        >
                                        <button
                                            @click="active_transact('toggle1')"
                                            class="h-6 flex items-center tracking-wide rounded py-1 flex text-xs hover:bg-gray-400 hover:text-white justify-start pl-4"
                                        >
                                            Offer #1
                                        </button>
                                        <button
                                            @click="active_transact('toggle2')"
                                            class="h-6 flex items-center tracking-wide rounded py=1 flex text-xs hover:bg-gray-400 hover:text-white justify-start pl-4"
                                        >
                                            Request #1
                                        </button>
                                    </div>

                                    <div class="flex flex-col pb-2">
                                        <span
                                            class="pl-1 font-semibold text-gray-500 py-1 py-1 text-xs tracking-wide"
                                            >Request(s)/Offers SENT</span
                                        >
                                        <button
                                            @click="active_transact('toggle3')"
                                            class="h-6 flex items-center tracking-wide rounded py-1 flex text-xs hover:bg-gray-400 hover:text-white justify-start pl-4"
                                        >
                                            Offer #1
                                        </button>
                                        <button
                                            @click="active_transact('toggle4')"
                                            class="h-6 flex items-center tracking-wide rounded py=1 flex text-xs hover:bg-gray-400 hover:text-white justify-start pl-4"
                                        >
                                            Request #1
                                        </button>
                                    </div>

                                    <div class="flex flex-col pb-2">
                                        <span
                                            class="pl-1 font-semibold text-gray-500 py-1 py-1 text-xs tracking-wide"
                                            >OTHER TRANSACTIONS</span
                                        >
                                        <button
                                            @click="active_transact('toggle5')"
                                            class="h-6 flex items-center tracking-wide rounded py-1 flex text-xs hover:bg-gray-400 hover:text-white text-blue-500 justify-start pl-4"
                                        >
                                            Tansactions #17
                                        </button>
                                        <button
                                            @click="active_transact('toggle6')"
                                            class="h-6 flex items-center tracking-wide rounded py=1 flex text-xs hover:bg-gray-400 hover:text-white text-crimsonRed justify-start pl-4"
                                        >
                                            Transactions #18
                                        </button>
                                        <span
                                            class="pl-4 font-semibold italic text-gray-400 py-1 py-1 text-xs"
                                            >No other transactions</span
                                        >
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-----end of transaction options--->
                    </div>
                    <!------------------->
                    <div
                        v-show="toggle"
                        id="delBtn"
                        class="absolute top-14 right-1.5 shadow-lg bg-gray-100 border-2 rounded w-56 flex flex-col justify-center text-sm"
                    >
                        <button
                            class="tracking-wide py-2 px-10 bg-gray-100 font-semibold hover:border-white hover:bg-crimsonRed hover:text-white p-2"
                        >
                            Delete
                        </button>
                        <button
                            v-if="!ifHide"
                            @click="showVertiOptions"
                            class="tracking-wide bg-gray-100 font-semibold hover:border-white hover:bg-crimsonRed hover:text-white p-2"
                        >
                            Show Transactions
                        </button>
                    </div>

                    <div class="p-2 flex justify-end">
                        <div
                            class="ml-32 pt-2 pl-4 pb-3 pr-4 text-sm bg-gray-200 rounded-lg"
                        >
                            <p>{{ chatOutgoing[0].sent }}</p>
                            <span
                                class="time_date text-gray-500 pl-1"
                                style="font-size: 10.5px"
                            >
                                {{ chatOutgoing[0].timeSent }}
                            </span>
                        </div>
                    </div>

                    <div class="flex justify-end mt-2">
                        <div class="ml-32 bg-gray-100 text-sm rounded-lg">
                            <div
                                class="flex flex-col bg-gray-200 py-2 rounded-lg"
                            >
                                <div class="mx-4 mb-2 text-sm font-semibold">
                                    <span>Order Details</span>
                                </div>
                                <div class="mx-4 pr-2 pt-3 pb-3 text-sm">
                                    <div class="flex flex-col px-2">
                                        <div class="flex items-start">
                                            <span
                                                class="text-red-700 material-icons"
                                                style="font-size: 18px"
                                                >place</span
                                            >
                                            <span class="pl-2 pb-1">
                                                {{ placeFrom }}</span
                                            >
                                        </div>
                                        <div class="flex items-start">
                                            <span
                                                class="text-red-700 material-icons"
                                                style="font-size: 18px"
                                                >shopping_cart</span
                                            >
                                            <span class="pl-2 pb-1"
                                                >SM {{ destination }}</span
                                            >
                                        </div>
                                        <div class="flex items-start">
                                            <span
                                                class="text-red-700 material-icons"
                                                style="font-size: 16px"
                                                >watch_later</span
                                            >
                                            <span class="pl-2 pb-1">{{
                                                timeAlloted
                                            }}</span>
                                        </div>
                                        <div class="flex items-start">
                                            <span
                                                class="text-red-700 material-icons"
                                                style="font-size: 16px"
                                                >payments</span
                                            >
                                            <span class="pl-2">{{
                                                paymentMethod
                                            }}</span>
                                        </div>
                                    </div>
                                </div>
                                <div
                                    class="mx-4 p-2 bg-white rounded-lg text-sm"
                                >
                                    <div>
                                        <span class="font-semibold"
                                            >Shopping List<span
                                                class="ml-3 text-gray-500"
                                                >{{
                                                    shoppingListSize
                                                }}items</span
                                            ></span
                                        >
                                    </div>
                                    <div>
                                        <ul
                                            class="text-gray-600 list-disc list-inside pl-4"
                                        >
                                            <li
                                                v-for="items in shoppingList"
                                                :key="items.ShoppingList"
                                            >
                                                <span>
                                                    {{ items.items }}
                                                </span>
                                            </li>
                                        </ul>
                                    </div>
                                    <div></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!----------------------------------------->
                    <div class="p-1 ml-12">
                        <div class="flex items-end pr-10 mt-1">
                            <div
                                class="flex flex-col bg-gray-100 py-2 rounded-lg"
                            >
                                <div>
                                    <div
                                        class="mx-4 mb-2 text-sm font-semibold"
                                    >
                                        <span>Order Details</span>
                                    </div>
                                    <div class="mx-4 pr-2 pt-3 pb-3 text-sm">
                                        <div class="flex flex-col px-2">
                                            <div class="flex items-start">
                                                <span
                                                    class="text-red-700 material-icons"
                                                    style="font-size: 18px"
                                                    >place</span
                                                >
                                                <span class="pl-2 pb-1">{{
                                                    placeFrom
                                                }}</span>
                                            </div>
                                            <div class="flex items-start">
                                                <span
                                                    class="text-red-700 material-icons"
                                                    style="font-size: 18px"
                                                    >shopping_cart</span
                                                >
                                                <span class="pl-2 pb-1">{{
                                                    destination
                                                }}</span>
                                            </div>
                                            <div class="flex items-start">
                                                <span
                                                    class="text-red-700 material-icons"
                                                    style="font-size: 16px"
                                                    >watch_later</span
                                                >
                                                <span class="pl-2 pb-1">{{
                                                    timeAlloted
                                                }}</span>
                                            </div>
                                            <div class="flex items-start">
                                                <span
                                                    class="text-red-700 material-icons"
                                                    style="font-size: 16px"
                                                    >payments</span
                                                >
                                                <span class="pl-2">{{
                                                    paymentMethod
                                                }}</span>
                                            </div>
                                        </div>
                                    </div>
                                    <div
                                        class="mx-4 p-2 bg-white rounded-lg text-sm"
                                    >
                                        <div>
                                            <span class="font-semibold"
                                                >Shopping List<span
                                                    class="ml-3 text-gray-500"
                                                    >8 items</span
                                                ></span
                                            >
                                        </div>
                                        <div>
                                            <ul
                                                class="text-gray-600 list-disc list-inside pl-4"
                                            >
                                                <li
                                                    v-for="items in shoppingList"
                                                    :key="items.ShoppingList"
                                                >
                                                    <span>
                                                        {{ items.items }}
                                                    </span>
                                                </li>
                                            </ul>
                                        </div>
                                        <div></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="p-1 pl-2">
                        <div class="flex items-end pr-10 mt-1">
                            <img
                                src="https://ptetutorials.com/images/user-profile.png"
                                alt="sunil"
                                class="rounded-lg h-8 w-8"
                            />
                            <div class="rounded-lg">
                                <div
                                    class="ml-4 mr-10 p-3 bg-gray-100 text-sm rounded-lg"
                                >
                                    <p>{{ chatIncoming[0].received }}</p>
                                    <span
                                        class="text-gray-500 pl-1"
                                        style="font-size: 10.5px"
                                        >{{
                                            chatIncoming[0].timeReceived
                                        }}</span
                                    >
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="p-2 flex justify-end">
                        <div
                            class="ml-32 pt-2 pl-4 pb-3 pr-4 bg-gray-200 text-sm rounded-lg"
                        >
                            <p>{{ chatOutgoing[1].sent }}</p>
                            <span
                                class="time_date text-gray-500 pl-1"
                                style="font-size: 10.5px"
                                >{{ chatOutgoing[1].timeSent }}</span
                            >
                        </div>
                    </div>
                    <div class="p-1 pl-2">
                        <div class="flex items-end pr-10 mt-1">
                            <img
                                src="https://ptetutorials.com/images/user-profile.png"
                                alt="sunil"
                                class="rounded-lg h-8 w-8"
                            />
                            <div class="rounded-lg">
                                <div
                                    class="ml-4 mr-10 p-3 bg-gray-100 text-sm rounded-lg"
                                >
                                    <p>{{ chatIncoming[1].received }}</p>
                                    <span
                                        class="text-gray-500 pl-1"
                                        style="font-size: 10.5px"
                                        >{{
                                            chatIncoming[1].timeReceived
                                        }}</span
                                    >
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="p-2 flex justify-end">
                        <div
                            class="ml-32 pt-2 pl-4 pb-3 pr-4 bg-gray-200 text-sm rounded-lg"
                        >
                            <p>{{ chatOutgoing[2].sent }}</p>
                            <span
                                class="time_date text-gray-500 pl-1"
                                style="font-size: 10.5px"
                            >
                                {{ chatOutgoing[2].timeSent }}
                            </span>
                        </div>
                    </div>
                    <div class="p-1 pl-2">
                        <div class="flex items-end pr-10 mt-1">
                            <img
                                src="https://ptetutorials.com/images/user-profile.png"
                                alt="sunil"
                                class="rounded-lg h-8 w-8"
                            />
                            <div class="rounded-lg">
                                <div
                                    class="ml-4 mr-10 p-3 bg-gray-100 text-sm rounded-lg"
                                >
                                    <p>{{ chatIncoming[2].received }}</p>
                                    <span
                                        class="text-gray-500 pl-1"
                                        style="font-size: 10.5px"
                                        >{{
                                            chatIncoming[2].timeReceived
                                        }}</span
                                    >
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="p-2 flex justify-end">
                        <div
                            class="ml-32 pt-2 pl-4 pb-3 pr-4 bg-gray-200 text-sm rounded-lg"
                        >
                            <p>{{ chatOutgoing[3].sent }}</p>
                            <span
                                class="time_date text-gray-500 pl-1"
                                style="font-size: 10.5px"
                            >
                                {{ chatOutgoing[3].timeSent }}</span
                            >
                        </div>
                    </div>
                    <div class="p-1 pl-2">
                        <div class="flex items-end pr-10 mt-1">
                            <img
                                src="https://ptetutorials.com/images/user-profile.png"
                                alt="sunil"
                                class="rounded-lg h-8 w-8"
                            />
                            <div class="rounded-lg">
                                <div
                                    class="ml-4 mr-10 p-3 bg-gray-100 text-sm rounded-lg"
                                >
                                    <p>{{ chatIncoming[3].received }}</p>
                                    <span
                                        class="text-gray-500 pl-1"
                                        style="font-size: 10.5px"
                                        >{{
                                            chatIncoming[3].timeReceived
                                        }}</span
                                    >
                                </div>
                            </div>
                        </div>
                    </div>
                    <div id="chatmsg-DESKTOP"></div>
                </div>
                <div v-if="attachment" class="sticky bottom-11">
                    <div
                        class="w-full bg-white bg-opacity-100 flex justify-start pt-2"
                    >
                        <div class="flex items-center">
                            <input
                                type="file"
                                id="fileInput"
                                accept=" .png .jpg .xls,.xlsx, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel"
                                style="display: none"
                            />
                            <button
                                id="attachFile"
                                @click="attachFile"
                                class="w-8 bg-gray-100 ml-3 mb-2 focus:outline-none hover:bg-white hover:text-red-700 rounded-md"
                            >
                                <span
                                    class="material-icons"
                                    style="font-size: 22px"
                                >
                                    attachment</span
                                >
                            </button>
                            <label
                                id="file"
                                class="text-sm font-semibold text-gray-500 pl-4 pb-1 pb-2"
                                >No file chosen yet</label
                            >
                        </div>
                    </div>
                </div>

                <div
                    class="pr-4 w-full absolute bottom-3 flex flex-cols justify-between items-center"
                    style="min-width: 400"
                >
                    <button
                        class="h-6 w-6 ml-4 mr-1 bg-gray-400 rounded-full focus:outline-none hover:text-white"
                        @click="attachbtn"
                        type="button"
                    >
                        <span class="material-icons" id="attach">
                            {{ attach }}</span
                        >
                    </button>
                    <input
                        type="text"
                        class="w-10/12 h-8 flex pl-4 border focus:outline-none focus:ring-1 focus:ring-gray-400 rounded-full"
                        placeholder="Type a message"
                        id="typemsg-DESKTOP"
                    />
                    <button
                        @click="sendbtn"
                        class="w-8 h-8 flex items-center pl-1 rounded-full focus:outline-none hover:text-red-700"
                        type="button"
                    >
                        <span class="material-icons"> send</span>
                    </button>
                </div>
            </div>
            <!--end of chat corner-->
        </div>
    </div>
    <!---MOBILE VERSION---->
    <div class="mobileVersion">
        <div v-show="toggleChat">
            <div
                class="bg-gray-50 flex h-full min-h-screen max-h-screen justify-center"
            >
                <!---Chat Corner-->
                <div
                    class="mt-20 shadow-md relative vsv:w-full vsvs:w-full x-v:w-full se:w-full vvs:w-full lvs:w-full vs:w-full ssm:w-full xsm:w-full sm:w-full mt-20 w-5/12 md:w-2/3"
                >
                    <div
                        class="relative flex justify-items-center md:justify-items-center shadow py-3"
                    >
                        <div class="flex flex-row justify-between">
                            <div class="flex flex-row">
                                <button
                                    id="backNavigator"
                                    class="focus:outline-none pl-5 hover:text-red-700"
                                    @click="backChat"
                                    type="button"
                                >
                                    <span
                                        class="material-icons pt-2"
                                        id="iMessage"
                                    >
                                        keyboard_backspace</span
                                    >
                                </button>

                                <h4 class="text-base font-bold pt-2 pl-4">
                                    {{ activeName }}
                                </h4>
                                <span
                                    class="material-icons pl-3 pt-3"
                                    id="iCheck"
                                >
                                    check_circle
                                </span>
                            </div>

                            <div class="align-middle absolute right-2">
                                <button
                                    @click="threedots"
                                    class="focus:bg-gray-300 hover:bg-gray-300 rounded-full px-1 h-6 mr-3 focus:outline-none hover:text-red-700"
                                    type="button"
                                >
                                    <span class="material-icons">
                                        more_horiz</span
                                    >
                                </button>
                            </div>
                        </div>
                    </div>

                    <div
                        class="overflow-auto overflow-x-hidden h-4/5"
                        id="journal-scroll"
                    >
                        <div
                            v-if="ifHide"
                            class="sticky top-0 p-3 flex justify items-center shadow-lg bg-white border"
                        >
                            <!-- sent offer 1--->
                            <div v-if="toggle1" class="text-sm w-full">
                                <div class="flex justify-between items-center">
                                    <span
                                        >You sent an offer to
                                        <span class="font-semibold ml-2">{{
                                            recipient
                                        }}</span>
                                        <span class="ml-2">for</span>
                                        <span class="font-semibold ml-2"
                                            >Post {{ postNum }}
                                        </span></span
                                    >

                                    <button
                                        @click="vertiDots"
                                        class="w-4 h-6 py-1 pb-1 pr-1 rounded-full focus:outline-none hover:text-red-700 hover:bg-gray-300 active:bg-gray-300"
                                        type="button"
                                    >
                                        <span
                                            class="material-icons"
                                            style="font-size: 17px"
                                        >
                                            more_verti</span
                                        >
                                    </button>
                                </div>

                                <div class="flex justify-end pr-3">
                                    <button
                                        @click="cancel_transact('offer')"
                                        class="mx-2 mt-2 h-7 px-2 hover:text-white hover:bg-gray-300 rounded-full border border-gray-700"
                                    >
                                        <span>Cancel Offer</span>
                                    </button>
                                    <router-link
                                        to="/dashboard"
                                        class="flex items-center mx-2 mt-2 h-7 px-2 hover:bg-gray-300 rounded-full bg-red-700 text-white"
                                        ><span>View Post</span></router-link
                                    >
                                </div>
                            </div>
                            <!------->
                            <!-- sent request 1--->
                            <div v-if="toggle2" class="text-sm w-full">
                                <div class="flex justify-between items-center">
                                    <span
                                        >You sent a request to
                                        <span class="font-semibold ml-2">{{
                                            recipient
                                        }}</span>
                                        <span class="ml-2">for</span>
                                        <span class="font-semibold ml-2"
                                            >Post {{ postNum }}
                                        </span></span
                                    >

                                    <button
                                        @click="vertiDots"
                                        class="w-4 h-6 py-1 pb-1 pr-1 rounded-full focus:outline-none hover:text-red-700 hover:bg-gray-300 active:bg-gray-300"
                                        type="button"
                                    >
                                        <span
                                            class="material-icons"
                                            style="font-size: 17px"
                                        >
                                            more_verti</span
                                        >
                                    </button>
                                </div>
                                <div class="flex justify-end pr-3">
                                    <button
                                        @click="cancel_transact('request')"
                                        class="mx-2 mt-2 h-7 px-2 hover:text-white hover:bg-gray-300 rounded-full border border-gray-700"
                                    >
                                        <span>Cancel Request</span>
                                    </button>
                                    <router-link
                                        to="/dashboard"
                                        class="flex items-center mx-2 mt-2 h-7 px-2 hover:bg-gray-300 rounded-full bg-red-700 text-white"
                                        ><span>View Post</span></router-link
                                    >
                                </div>
                            </div>
                            <!------->
                            <!-- received offer 1--->
                            <div v-if="toggle3" class="text-sm w-full">
                                <div class="flex justify-between items-center">
                                    <span
                                        ><span class="font-semibold mr-2">{{
                                            sender
                                        }}</span
                                        >sent you an offer
                                        <span class="ml-2">for your </span>
                                        <span class="font-semibold ml-2"
                                            >Post {{ postNum2 }}
                                        </span></span
                                    >
                                    <button
                                        @click="vertiDots"
                                        class="w-4 h-6 py-1 pb-1 pr-1 rounded-full focus:outline-none hover:text-red-700 hover:bg-gray-300 active:bg-gray-300"
                                        type="button"
                                    >
                                        <span
                                            class="material-icons"
                                            style="font-size: 17px"
                                        >
                                            more_verti</span
                                        >
                                    </button>
                                </div>
                                <div class="flex justify-end pr-3">
                                    <button
                                        @click="declineDisOffer('offer')"
                                        class="mx-2 mt-2 h-7 px-2 hover:text-white hover:bg-gray-300 focus:outline-none rounded-full border border-gray-700"
                                    >
                                        <span>Decline</span>
                                    </button>
                                    <button
                                        @click="acceptDisOffer('offer')"
                                        class="mx-2 mt-2 h-7 px-2 hover:bg-gray-300 rounded-full focus:outline-none bg-red-700 text-white"
                                    >
                                        <span>Accept</span>
                                    </button>
                                </div>
                            </div>
                            <!------->
                            <!-- received request 1--->
                            <div v-if="toggle4" class="text-sm w-full">
                                <div class="flex justify-between items-center">
                                    <span
                                        ><span class="font-semibold mr-2">{{
                                            sender
                                        }}</span
                                        >sent you a request
                                        <span class="ml-2">for your </span>
                                        <span class="font-semibold ml-2"
                                            >Post {{ postNum2 }}
                                        </span></span
                                    >
                                    <button
                                        @click="vertiDots"
                                        class="w-4 h-6 py-1 pb-1 pr-1 rounded-full focus:outline-none hover:text-red-700 hover:bg-gray-300 active:bg-gray-300"
                                        type="button"
                                    >
                                        <span
                                            class="material-icons"
                                            style="font-size: 17px"
                                        >
                                            more_verti</span
                                        >
                                    </button>
                                </div>
                                <div class="flex justify-end pr-3">
                                    <button
                                        @click="declineDisOffer('request')"
                                        class="mx-2 mt-2 h-7 px-2 hover:text-white hover:bg-gray-300 focus:outline-none rounded-full border border-gray-700"
                                    >
                                        <span>Decline</span>
                                    </button>
                                    <button
                                        @click="acceptDisOffer('request')"
                                        class="mx-2 mt-2 h-7 px-2 hover:bg-gray-300 rounded-full focus:outline-none bg-red-700 text-white"
                                    >
                                        <span>Accept</span>
                                    </button>
                                </div>
                            </div>
                            <!------->

                            <!--------------transaction details confirmed------>
                            <div v-if="toggle5" class="text-sm w-full">
                                <div class="flex flex-row justify-between">
                                    <span
                                        >Transaction
                                        <span class="font-semibold ml-2"
                                            >{{ postNum2 }}
                                        </span>
                                    </span>

                                    <div class="flex items-center">
                                        <span
                                            class="rounded border h-6 border-blue-700 px-1"
                                            >Confirmed</span
                                        >

                                        <button
                                            @click="vertiDots"
                                            class="w-4 h-6 py-1 pb-1 pr-1 rounded-full focus:outline-none hover:text-red-700 hover:bg-gray-300 active:bg-gray-300"
                                            type="button"
                                        >
                                            <span
                                                class="material-icons"
                                                style="font-size: 17px"
                                            >
                                                more_verti</span
                                            >
                                        </button>
                                    </div>
                                </div>
                                <div class="flex justify-end pr-3">
                                    <button
                                        @click="toggleViewDetails"
                                        class="mx-2 mt-2 h-7 px-2 hover:text-white hover:bg-gray-300 focus:outline-none rounded-full border border-gray-700"
                                    >
                                        <span>View Details</span>
                                    </button>
                                    <button
                                        @click="
                                            (toggle_status = !toggle_status),
                                                (trans_id = itemx.id)
                                        "
                                        class="mx-2 mt-2 h-7 px-2 hover:bg-gray-300 rounded-full focus:outline-none bg-red-700 text-white"
                                    >
                                        <span>Update</span>
                                    </button>
                                </div>
                            </div>
                            <!------------------->

                            <!--------------transaction details cancelled------>
                            <div v-if="toggle6" class="text-sm w-full">
                                <div class="flex flex-row justify-between">
                                    <span
                                        >Transaction
                                        <span class="font-semibold ml-2"
                                            >{{ postNum2 }}
                                        </span>
                                    </span>

                                    <div class="flex items-center">
                                        <span
                                            class="rounded border h-6 border-crimsonRed text-crimsonRed px-1"
                                            >Cancelled</span
                                        >

                                        <button
                                            @click="vertiDots"
                                            class="w-4 h-6 py-1 pb-1 pr-1 rounded-full focus:outline-none hover:text-red-700 hover:bg-gray-300 active:bg-gray-300"
                                            type="button"
                                        >
                                            <span
                                                class="material-icons"
                                                style="font-size: 17px"
                                            >
                                                more_verti</span
                                            >
                                        </button>
                                    </div>
                                </div>
                                <div class="flex justify-end pr-3">
                                    <button
                                        @click="toggleViewDetails"
                                        class="mx-2 mt-2 h-7 px-2 hover:text-white hover:bg-gray-300 focus:outline-none rounded-full border border-gray-700"
                                    >
                                        <span>View Details</span>
                                    </button>
                                    <button
                                        @click="VOID"
                                        class="bg-opacity-50 mx-2 mt-2 h-7 px-2 rounded-full focus:outline-none bg-red-700 text-white"
                                    >
                                        <span>Update</span>
                                    </button>
                                </div>
                            </div>
                            <!------------------->
                            <!-----vertical-dot  options-->
                            <div
                                v-if="toggleVerti"
                                id="vertiOPTIONS-MOBILE"
                                class="absolute right-4 top-2 xl:fixed xl:top-36 xl:right-16 px-2 mr-4 bg-gray-200 w-2/5 shadow-inner rounded-lg border-solid border-2 border-white"
                                style="width: 220px"
                            >
                                <div class="flex flex-col">
                                    <div class="flex flex-row items-center">
                                        <button
                                            @click="hideVertiOptions"
                                            class="w-full items-center flex py-1 hover:bg-white hover:text-crimsonRed justify-start mt-2 border border-gray-300 rounded-lg"
                                        >
                                            <span
                                                class="material-icons pl-3"
                                                style="font-size: 20px"
                                                >visibility</span
                                            >
                                            <span class="font-semibold pl-2"
                                                >Hide</span
                                            >
                                        </button>
                                    </div>
                                    <div
                                        class="divide-y divide-gray-300 tracking-wide"
                                    >
                                        <div class="flex flex-col pb-2">
                                            <span
                                                class="pl-1 font-semibold py-1 text-gray-500 py-1 text-xs"
                                                >Request(s)/Offers
                                                RECEIVED</span
                                            >
                                            <button
                                                @click="
                                                    active_transact('toggle1')
                                                "
                                                class="h-6 flex items-center rounded tracking-wide py-1 flex text-xs hover:bg-gray-400 hover:text-white justify-start pl-4"
                                            >
                                                Offer #1
                                            </button>
                                            <button
                                                @click="
                                                    active_transact('toggle2')
                                                "
                                                class="h-6 flex items-center rounded tracking-wide py-1 flex text-xs hover:bg-gray-400 hover:text-white justify-start pl-4"
                                            >
                                                Request #1
                                            </button>
                                        </div>

                                        <div class="flex flex-col pb-2">
                                            <span
                                                class="pl-1 font-semibold text-gray-500 py-1 py-1 text-xs"
                                                >Request(s)/Offers SENT</span
                                            >
                                            <button
                                                @click="
                                                    active_transact('toggle3')
                                                "
                                                class="h-6 flex items-center rounded tracking-wide py-1 flex text-xs hover:bg-gray-400 hover:text-white justify-start pl-4"
                                            >
                                                Offer #1
                                            </button>
                                            <button
                                                @click="
                                                    active_transact('toggle4')
                                                "
                                                class="h-6 flex items-center rounded tracking-wide py-1 flex text-xs hover:bg-gray-400 hover:text-white justify-start pl-4"
                                            >
                                                Request #1
                                            </button>
                                        </div>

                                        <div class="flex flex-col pb-2">
                                            <span
                                                class="pl-1 font-semibold text-gray-500 py-1 py-1 text-xs"
                                                >OTHER TRANSACTIONS</span
                                            >
                                            <button
                                                @click="
                                                    active_transact('toggle5')
                                                "
                                                class="h-6 flex items-center rounded tracking-wide py-1 flex text-xs hover:bg-gray-400 hover:text-white text-blue-500 justify-start pl-4"
                                            >
                                                Tansactions #17
                                            </button>
                                            <button
                                                @click="
                                                    active_transact('toggle6')
                                                "
                                                class="h-6 flex items-center rounded tracking-wide py-1 flex text-xs hover:bg-gray-400 hover:text-white text-crimsonRed justify-start pl-4"
                                            >
                                                Transactions #18
                                            </button>
                                            <span
                                                class="pl-4 font-semibold italic text-gray-400 py-1 py-1 text-xs"
                                                >No other transactions</span
                                            >
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-----end of transaction options--->
                        </div>
                        <!------------------->

                        <div
                            v-show="toggle"
                            id="delBtn-MOBILE"
                            class="absolute top-16 right-1.5 shadow-lg bg-gray-100 border-2 rounded w-56 flex flex-col justify-center text-sm"
                        >
                            <button
                                class="tracking-wide bg-gray-100 font-semibold hover:border-white hover:bg-crimsonRed hover:text-white p-2"
                            >
                                Delete
                            </button>
                            <button
                                v-if="!ifHide"
                                @click="showVertiOptions"
                                class="tracking-wide bg-gray-100 font-semibold hover:border-white hover:bg-crimsonRed hover:text-white p-2"
                            >
                                Show Transactions
                            </button>
                        </div>

                        <div class="p-2 flex justify-end">
                            <div
                                class="ml-32 pt-2 pl-4 pb-3 pr-4 text-sm bg-gray-200 rounded-lg"
                            >
                                <p>{{ chatOutgoing[0].sent }}</p>
                                <span
                                    class="time_date text-gray-500 pl-1"
                                    style="font-size: 10.5px"
                                >
                                    {{ chatOutgoing[0].timeSent }}
                                </span>
                            </div>
                        </div>

                        <div class="flex justify-end mt-2">
                            <div class="ml-32 bg-gray-100 text-sm rounded-lg">
                                <div
                                    class="flex flex-col bg-gray-200 py-2 rounded-lg"
                                >
                                    <div
                                        class="mx-4 mb-2 text-sm font-semibold"
                                    >
                                        <span>Order Details</span>
                                    </div>
                                    <div class="mx-4 pr-2 pt-3 pb-3 text-sm">
                                        <div class="flex flex-col px-2">
                                            <div class="flex items-start">
                                                <span
                                                    class="text-red-700 material-icons"
                                                    style="font-size: 18px"
                                                    >place</span
                                                >
                                                <span class="pl-2 pb-1">
                                                    {{ placeFrom }}</span
                                                >
                                            </div>
                                            <div class="flex items-start">
                                                <span
                                                    class="text-red-700 material-icons"
                                                    style="font-size: 18px"
                                                    >shopping_cart</span
                                                >
                                                <span class="pl-2 pb-1"
                                                    >SM {{ destination }}</span
                                                >
                                            </div>
                                            <div class="flex items-start">
                                                <span
                                                    class="text-red-700 material-icons"
                                                    style="font-size: 16px"
                                                    >watch_later</span
                                                >
                                                <span class="pl-2 pb-1">{{
                                                    timeAlloted
                                                }}</span>
                                            </div>
                                            <div class="flex items-start">
                                                <span
                                                    class="text-red-700 material-icons"
                                                    style="font-size: 16px"
                                                    >payments</span
                                                >
                                                <span class="pl-2">{{
                                                    paymentMethod
                                                }}</span>
                                            </div>
                                        </div>
                                    </div>
                                    <div
                                        class="mx-4 p-2 bg-white rounded-lg text-sm"
                                    >
                                        <div>
                                            <span class="font-semibold"
                                                >Shopping List<span
                                                    class="ml-3 text-gray-500"
                                                    >{{
                                                        shoppingListSize
                                                    }}items</span
                                                ></span
                                            >
                                        </div>
                                        <div>
                                            <ul
                                                class="text-gray-600 list-disc list-inside pl-4"
                                            >
                                                <li
                                                    v-for="items in shoppingList"
                                                    :key="items.ShoppingList"
                                                >
                                                    <span>
                                                        {{ items.items }}
                                                    </span>
                                                </li>
                                            </ul>
                                        </div>
                                        <div></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!----------------------------------------->
                        <div class="p-1 ml-12">
                            <div class="flex items-end pr-10 mt-1">
                                <div
                                    class="flex flex-col bg-gray-100 py-2 rounded-lg"
                                >
                                    <div>
                                        <div
                                            class="mx-4 mb-2 text-sm font-semibold"
                                        >
                                            <span>Order Details</span>
                                        </div>
                                        <div
                                            class="mx-4 pr-2 pt-3 pb-3 text-sm"
                                        >
                                            <div class="flex flex-col px-2">
                                                <div class="flex items-start">
                                                    <span
                                                        class="text-red-700 material-icons"
                                                        style="font-size: 18px"
                                                        >place</span
                                                    >
                                                    <span class="pl-2 pb-1">{{
                                                        placeFrom
                                                    }}</span>
                                                </div>
                                                <div class="flex items-start">
                                                    <span
                                                        class="text-red-700 material-icons"
                                                        style="font-size: 18px"
                                                        >shopping_cart</span
                                                    >
                                                    <span class="pl-2 pb-1">{{
                                                        destination
                                                    }}</span>
                                                </div>
                                                <div class="flex items-start">
                                                    <span
                                                        class="text-red-700 material-icons"
                                                        style="font-size: 16px"
                                                        >watch_later</span
                                                    >
                                                    <span class="pl-2 pb-1">{{
                                                        timeAlloted
                                                    }}</span>
                                                </div>
                                                <div class="flex items-start">
                                                    <span
                                                        class="text-red-700 material-icons"
                                                        style="font-size: 16px"
                                                        >payments</span
                                                    >
                                                    <span class="pl-2">{{
                                                        paymentMethod
                                                    }}</span>
                                                </div>
                                            </div>
                                        </div>
                                        <div
                                            class="mx-4 p-2 bg-white rounded-lg text-sm"
                                        >
                                            <div>
                                                <span class="font-semibold"
                                                    >Shopping List<span
                                                        class="ml-3 text-gray-500"
                                                        >8 items</span
                                                    ></span
                                                >
                                            </div>
                                            <div>
                                                <ul
                                                    class="text-gray-600 list-disc list-inside pl-4"
                                                >
                                                    <li
                                                        v-for="items in shoppingList"
                                                        :key="
                                                            items.ShoppingList
                                                        "
                                                    >
                                                        <span>
                                                            {{ items.items }}
                                                        </span>
                                                    </li>
                                                </ul>
                                            </div>
                                            <div></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="p-1 pl-2">
                            <div class="flex items-end pr-10 mt-1">
                                <img
                                    src="https://ptetutorials.com/images/user-profile.png"
                                    alt="sunil"
                                    class="rounded-lg h-8 w-8"
                                />
                                <div class="rounded-lg">
                                    <div
                                        class="ml-4 mr-10 p-3 bg-gray-100 text-sm rounded-lg"
                                    >
                                        <p>{{ chatIncoming[0].received }}</p>
                                        <span
                                            class="text-gray-500 pl-1"
                                            style="font-size: 10.5px"
                                            >{{
                                                chatIncoming[0].timeReceived
                                            }}</span
                                        >
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="p-2 flex justify-end">
                            <div
                                class="ml-32 pt-2 pl-4 pb-3 pr-4 bg-gray-200 text-sm rounded-lg"
                            >
                                <p>{{ chatOutgoing[1].sent }}</p>
                                <span
                                    class="time_date text-gray-500 pl-1"
                                    style="font-size: 10.5px"
                                    >{{ chatOutgoing[1].timeSent }}</span
                                >
                            </div>
                        </div>
                        <div class="p-1 pl-2">
                            <div class="flex items-end pr-10 mt-1">
                                <img
                                    src="https://ptetutorials.com/images/user-profile.png"
                                    alt="sunil"
                                    class="rounded-lg h-8 w-8"
                                />
                                <div class="rounded-lg">
                                    <div
                                        class="ml-4 mr-10 p-3 bg-gray-100 text-sm rounded-lg"
                                    >
                                        <p>{{ chatIncoming[1].received }}</p>
                                        <span
                                            class="text-gray-500 pl-1"
                                            style="font-size: 10.5px"
                                            >{{
                                                chatIncoming[1].timeReceived
                                            }}</span
                                        >
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="p-2 flex justify-end">
                            <div
                                class="ml-32 pt-2 pl-4 pb-3 pr-4 bg-gray-200 text-sm rounded-lg"
                            >
                                <p>{{ chatOutgoing[2].sent }}</p>
                                <span
                                    class="time_date text-gray-500 pl-1"
                                    style="font-size: 10.5px"
                                >
                                    {{ chatOutgoing[2].timeSent }}
                                </span>
                            </div>
                        </div>
                        <div class="p-1 pl-2">
                            <div class="flex items-end pr-10 mt-1">
                                <img
                                    src="https://ptetutorials.com/images/user-profile.png"
                                    alt="sunil"
                                    class="rounded-lg h-8 w-8"
                                />
                                <div class="rounded-lg">
                                    <div
                                        class="ml-4 mr-10 p-3 bg-gray-100 text-sm rounded-lg"
                                    >
                                        <p>{{ chatIncoming[2].received }}</p>
                                        <span
                                            class="text-gray-500 pl-1"
                                            style="font-size: 10.5px"
                                            >{{
                                                chatIncoming[2].timeReceived
                                            }}</span
                                        >
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="p-2 flex justify-end">
                            <div
                                class="ml-32 pt-2 pl-4 pb-3 pr-4 bg-gray-200 text-sm rounded-lg"
                            >
                                <p>{{ chatOutgoing[3].sent }}</p>
                                <span
                                    class="time_date text-gray-500 pl-1"
                                    style="font-size: 10.5px"
                                >
                                    {{ chatOutgoing[3].timeSent }}</span
                                >
                            </div>
                        </div>
                        <div class="p-1 pl-2">
                            <div class="flex items-end pr-10 mt-1">
                                <img
                                    src="https://ptetutorials.com/images/user-profile.png"
                                    alt="sunil"
                                    class="rounded-lg h-8 w-8"
                                />
                                <div class="rounded-lg">
                                    <div
                                        class="ml-4 mr-10 p-3 bg-gray-100 text-sm rounded-lg"
                                    >
                                        <p>{{ chatIncoming[3].received }}</p>
                                        <span
                                            class="text-gray-500 pl-1"
                                            style="font-size: 10.5px"
                                            >{{
                                                chatIncoming[3].timeReceived
                                            }}</span
                                        >
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div id="chatmsg-MOBILE"></div>
                    </div>
                    <div v-if="attachment" class="sticky bottom-11">
                        <div
                            class="w-full bg-white bg-opacity-100 flex justify-start pt-2"
                        >
                            <div class="flex items-center">
                                <input
                                    type="file"
                                    id="fileInput"
                                    accept=" .png .jpg .xls,.xlsx, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel"
                                    style="display: none"
                                />
                                <button
                                    id="attachFile"
                                    @click="attachFile"
                                    class="w-8 bg-gray-100 ml-3 mb-2 focus:outline-none hover:bg-white hover:text-red-700 rounded-md"
                                >
                                    <span
                                        class="material-icons"
                                        style="font-size: 22px"
                                    >
                                        attachment</span
                                    >
                                </button>
                                <label
                                    id="file"
                                    class="text-sm font-semibold text-gray-500 pl-4 pb-1 pb-2"
                                    >No file chosen yet</label
                                >
                            </div>
                        </div>
                    </div>

                    <div
                        class="pr-4 w-full absolute bottom-3 flex flex-cols justify-between items-center"
                        style="min-width: 400"
                    >
                        <button
                            class="h-6 w-6 ml-4 mr-1 bg-gray-400 rounded-full focus:outline-none hover:text-white"
                            @click="attachbtn"
                            type="button"
                        >
                            <span class="material-icons" id="attach2">
                                {{ attach }}</span
                            >
                        </button>
                        <input
                            type="text"
                            class="w-10/12 h-8 flex pl-4 border focus:outline-none focus:ring-1 focus:ring-gray-400 rounded-full"
                            placeholder="Type a message"
                            id="typemsg-MOBILE"
                        />
                        <button
                            @click="sendbtn"
                            class="w-8 h-8 flex items-center pl-1 rounded-full focus:outline-none hover:text-red-700"
                            type="button"
                        >
                            <span class="material-icons"> send</span>
                        </button>
                    </div>
                </div>
                <!--end of right corner-->
            </div>
        </div>
        <!-------------end chatbox------------->
        <div v-show="toggleInbox">
            <div
                class="bg-gray-50 flex h-full min-h-screen max-h-screen w-full justify-center pb-2"
            >
                <!--Inbox Corner-->
                <div
                    class="mt-20 shadow-md vsv:w-full vsvs:w-full x-v:w-full se:w-full vvs:w-full lvs:w-full vs:w-full ssm:w-full xsm:w-full sm:w-full mt-20 md:w-1/3 relative"
                >
                    <div
                        id="msgheader"
                        class="flex justify-items-center relative shadow pt-5 pb-1"
                    >
                        <button
                            class="focus:outline-none pl-5 hover:text-red-700"
                            type="button"
                        >
                            <span class="material-icons pt-1" id="iMessage">
                                chat</span
                            >
                        </button>
                        <h4 class="tracking-wider text-base font-bold pl-4">
                            Message
                        </h4>
                    </div>

                    <div
                        v-if="searchMessageInactive"
                        class="flex justify-center w-full relative py-1 mt-2 pt-2"
                    >
                        <input
                            type="text"
                            class="h-8 w-11/12 pl-5 border font-normal text-sm focus:outline-none focus:ring-1 focus:ring-gray-300 rounded-full"
                            placeholder="Search"
                        />
                        <button
                            @click="searchBtn"
                            class="align-middle absolute right-8 pt-1 h-7 focus:outline-none hover:text-red-700"
                        >
                            <span
                                class="material-icons"
                                style="font-size: 22px"
                            >
                                search
                            </span>
                        </button>
                    </div>
                    <!---end of search bar-->

                    <button
                        v-if="showSearchResults"
                        class="flex justify-center w-full relative py-1 mt-2 pt-2 focus:outline-none"
                    >
                        <input
                            type="text"
                            class="h-8 w-10/12 pl-5 border font-normal text-sm focus:outline-none focus:ring-1 focus:ring-gray-300 rounded-full"
                            placeholder="Mark"
                            id="search"
                        />
                        <button
                            class="align-middle mt-1 ml-1 flex items-center h-6 w-6 rounded-full bg-gray-300 focus:outline-none hover:text-red-700"
                        >
                            <span
                                @click="closeSearchResults"
                                class="material-icons pl-1"
                                style="font-size: 17px"
                            >
                                close
                            </span>
                        </button></button
                    ><!---end of search bar-->

                    <div
                        class="overflow-auto overflow-x-hidden px-0 py-1 h-4/5"
                        id="scrollInbox"
                    >
                        <div v-if="searchMessageInactive">
                            <button
                                @click="active_convo('Mark Aral')"
                                type="button"
                                class="focus:bg-gray-200 relative w-full sm:pr-8 flex focus:outline-none justify-between items-center mt-2 p-2 hover:shadow-lg cursor-pointer transition"
                            >
                                <div class="flex ml-2">
                                    <img
                                        src="https://ptetutorials.com/images/user-profile.png"
                                        alt="sunil"
                                        class="rounded-lg h-8 w-7 pt-1"
                                    />
                                    <div
                                        class="flex flex-col justify-between items-start ml-2"
                                    >
                                        <span
                                            class="font-medium text-sm"
                                            id="mark"
                                        >
                                            {{ inbox[0].name }}
                                            <span
                                                class="material-icons pl-2"
                                                id="iCheck"
                                                style="font-size: 14px"
                                            >
                                                check_circle
                                            </span></span
                                        >
                                        <span
                                            class="text-xs text-gray-400 truncate w-36 md:w-28 lvs:w-64 sm:w-64 ssm:w-24"
                                        >
                                            {{ inbox[0].message }}
                                        </span>
                                    </div>
                                </div>
                                <div class="flex flex-col items-start">
                                    <span class="text-gray-700 text-xs">
                                        <span class="font-bold pl-1 pr-1"
                                            >·</span
                                        >{{ inbox[0].time }}</span
                                    >
                                </div>
                            </button>

                            <button
                                @click="active_convo('Gwen Lopez')"
                                type="button"
                                class="focus:bg-gray-200 relative w-full sm:pr-8 flex focus:outline-none justify-between items-center mt-2 p-2 hover:shadow-lg cursor-pointer transition"
                            >
                                <div class="flex ml-2">
                                    <img
                                        src="https://ptetutorials.com/images/user-profile.png"
                                        alt="sunil"
                                        class="rounded-lg h-8 w-7 pt-1"
                                    />
                                    <div
                                        class="flex flex-col justify-between items-start ml-2"
                                    >
                                        <span
                                            class="font-medium text-sm"
                                            id="gwen"
                                            >{{ inbox[1].name
                                            }}<span
                                                class="material-icons pl-2"
                                                id="iCheck"
                                                style="font-size: 14px"
                                            >
                                                check_circle
                                            </span></span
                                        >
                                        <span
                                            class="text-xs text-gray-400 truncate w-32 md:w-28 lvs:w-64 sm:w-64 ssm:w-24"
                                        >
                                            {{ inbox[1].message }}
                                        </span>
                                    </div>
                                </div>
                                <div class="flex flex-col items-start">
                                    <span class="text-gray-700 text-xs">
                                        <span class="font-bold pl-1 pr-1"
                                            >·</span
                                        >{{ inbox[1].time }}</span
                                    >
                                </div>
                            </button>
                        </div>
                        <!---------------navigation message------------>

                        <div
                            v-if="showSearchResults"
                            class="divide-y divide-gray-300"
                        >
                            <div
                                class="py-2 flex justify-center font-normal text-xs italic"
                            >
                                <span>Search Results</span>
                            </div>
                            <div>
                                <button
                                    @click="Void"
                                    type="button"
                                    class="focus:bg-gray-200 relative w-full flex sm:pr-8 focus:outline-none justify-between items-center mt-2 p-2 hover:shadow-lg cursor-pointer transition"
                                >
                                    <div class="flex ml-2">
                                        <img
                                            src="https://ptetutorials.com/images/user-profile.png"
                                            alt="sunil"
                                            class="rounded-lg h-8 w-7 pt-1"
                                        />
                                        <div
                                            class="flex flex-col justify-between items-start ml-2"
                                        >
                                            <span
                                                class="font-medium text-sm italic"
                                                id="mark"
                                            >
                                                <span class="text-red-700"
                                                    >Mark</span
                                                >
                                                Aral
                                                <span
                                                    class="material-icons pl-2"
                                                    id="iCheck"
                                                >
                                                    check_circle
                                                </span></span
                                            >
                                            <span
                                                class="text-xs text-gray-400 truncate md:w-28 w-36 lvs:w-64 sm:w-72 ssm:w-24"
                                            >
                                                {{ inbox[0].message }}
                                            </span>
                                        </div>
                                    </div>
                                    <div class="flex flex-col items-start">
                                        <span class="text-gray-700 text-xs">
                                            <span class="font-bold pl-1 pr-1"
                                                >·</span
                                            >{{ inbox[0].time }}</span
                                        >
                                    </div>
                                </button>
                            </div>
                        </div>
                        <!---------------search message results------------>
                    </div>
                </div>
                <!--end of left corner-->
            </div>
        </div>
    </div>

    <!--Accept User Request Modal-->
    <div
        v-if="viewDetails"
        class="z-50 fixed bg-black bg-opacity-25 inset-0 flex justify-center items-center ssm:px-2 vs:px-2"
    >
        <div
            class="hideMe1 inline-flex flex-col bg-white shadow rounded-xl h-auto w-97 space-y-4 p-4 ssm:w-full vs:w-full"
        >
            <div class="flex justify-between items-center flex-row">
                <button
                    class="invisible focus:outline-none text-sm font-bold leading-none text-right text-indigo-900"
                >
                    Back</button
                ><!--invisible, used only for auto margin header. If design need close button just delete the invisible class-->
                <p
                    class="text-lg ssm:text-sm vs:text-base font-bold leading-normal text-center text-gray-900"
                >
                    Request from Asta
                </p>
                <button
                    @click="toggleViewDetails"
                    class="focus:outline-none text-sm font-bold leading-none text-right text-indigo-900"
                >
                    Close
                </button>
            </div>
            <hr class="w-full" />
            <div class="flex w-full flex-row items-center space-x-4">
                <img src="img/asta.jpeg" class="rounded-full w-10 h-10" />
                <div class="flex flex-col">
                    <div class="flex-row flex space-x-1 items-center">
                        <p
                            class="text-base font-bold leading-none text-gray-900"
                        >
                            Asta Staria
                        </p>
                        <span
                            class="text-blue-900 align-middle material-icons text-base"
                        >
                            verified
                        </span>
                    </div>
                    <p class="text-sm leading-none text-gray-500">
                        5 minutes ago
                    </p>
                </div>
            </div>
            <div class="flex flex-col w-full">
                <div class="flex space-x-2">
                    <span
                        class="w-6 h-6 rounded-full material-icons text-red-600"
                    >
                        location_on
                    </span>
                    <p
                        class="text-sm ssm:text-xs vs:text-xs lvs:text-sm leading-none text-gray-900 py-1"
                    >
                        {{ request_info.delivery_area }}
                    </p>
                </div>
                <div class="flex space-x-2 py-2">
                    <span
                        class="w-6 h-6 rounded-full material-icons text-red-600"
                    >
                        alarm
                    </span>
                    <p
                        class="text-sm ssm:text-xs vs:text-xs lvs:text-sm leading-none text-gray-900 py-1"
                    >
                        {{ request_info.schedule }}
                    </p>
                </div>
                <div class="flex space-x-2">
                    <span
                        class="w-6 h-6 rounded-full material-icons text-red-600"
                    >
                        shopping_cart
                    </span>
                    <p
                        class="text-sm ssm:text-xs vs:text-xs lvs:text-sm leading-none text-gray-900 py-1"
                    >
                        {{ request_info.shopping_place }}
                    </p>
                </div>
                <div class="flex space-x-2 py-2">
                    <span
                        class="w-6 h-6 rounded-full material-icons text-red-600"
                    >
                        payments
                    </span>
                    <p
                        class="text-sm ssm:text-xs vs:text-xs lvs:text-sm leading-none text-gray-900 py-1"
                    >
                        {{ request_info.payment_method }}
                    </p>
                </div>
            </div>
            <div
                class="flex flex-col ssm:mt-2 vs:mt-2 mt-3 w-full items-start justify-start h-auto vs:pr-0 vs:min-w-0 vs:px-2 ssm:pr-0 ssm:min-w-0 ssm:px-2 p-4 bg-gray-100 rounded-xl"
            >
                <div class="inline-flex flex-row space-x-4">
                    <span
                        class="text-base ssm:text-sm leading-none text-gray-900"
                        >Shopping List</span
                    >
                    <span
                        class="text-base ssm:text-sm leading-none text-gray-500"
                        >{{ countItems }} items</span
                    >
                </div>
                <div
                    class="inline-flex flex-col ssm:px-0 w-full vs:px-0 space-y-2 py-4 px-4"
                >
                    <li
                        v-for="shoppingItems in computedShopItemList"
                        :key="shoppingItems"
                        class="text-sm leading-none text-gray-900"
                    >
                        {{ shoppingItems.item }} ({{ shoppingItems.amount }}) ·
                        {{ shoppingItems.brand }} [{{ shoppingItems.unit }}]
                    </li>
                </div>
                <button
                    @click="showMoreshowLess"
                    v-if="!isFew"
                    class="focus:outline-none items-start justify-start text-sm text-gray-500"
                >
                    {{ showListStatus }}
                </button>
            </div>
            <div
                class="inline-flex items-start ssm:px-2 justify-start mt-3 rounded-xl h-auto bg-white w-full"
            >
                <p
                    class="text-sm ssm:text-xs vs:text-xs lvs:text-sm leading-normal w-auto text-gray-900"
                >
                    {{ request_info.comment }}
                </p>
            </div>
            <div
                class="justify-between flex flex-row vs:space-x-2 ssm:space-x-2 sm:space-x-2 w-full"
            >
                <button
                    @click="declineDisRequest"
                    class="focus:outline-none inline-flex items-center justify-center w-52 px-3 py-1 border-2 rounded-full border-red-700"
                >
                    <p
                        class="text-base font-bold leading-normal text-center text-gray-900"
                    >
                        Decline
                    </p>
                </button>
                <button
                    @click="acceptDisRequest"
                    class="focus:outline-none inline-flex items-center justify-center w-52 px-3 py-1 bg-red-700 rounded-full"
                >
                    <p
                        class="text-base font-bold leading-normal text-center text-white"
                    >
                        Accept
                    </p>
                </button>
            </div>
        </div>
    </div>
    <!--end-->

    <!--Accept User Request Button Modal-->
    <transition name="fadeSlide">
        <div
            v-if="acceptRequest"
            class="z-50 fixed inset-0 flex justify-center items-center ssm:px-2 vs:px-2"
        >
            <div
                class="inline-flex flex-col bg-white shadow rounded-xl h-auto w-95 space-y-4 p-4 ssm:w-full vs:w-full"
            >
                <div class="flex justify-between items-center flex-row">
                    <button
                        class="invisible focus:outline-none text-sm font-bold leading-none text-right text-indigo-900"
                    >
                        Back</button
                    ><!--invisible, used only for auto margin header. If design need close button just delete the invisible class-->
                    <p
                        class="text-lg ssm:text-sm vs:text-base font-bold leading-normal text-center text-gray-900"
                    >
                        Accept Asta's Request
                    </p>
                    <button
                        @click="acceptDisRequest1"
                        class="focus:outline-none text-sm font-bold leading-none text-right text-indigo-900"
                    >
                        Close
                    </button>
                </div>
                <hr class="w-full" />
                <div class="flex w-full">
                    <p
                        class="block items-start leading-normal text-base text-gray-900"
                    >
                        Are you sure you want to accept Asta's request?
                    </p>
                </div>
                <div class="justify-between flex flex-row space-x-2 w-full">
                    <button
                        @click="acceptDisRequest1"
                        class="focus:outline-none inline-flex items-center justify-center w-52 px-3 py-1 border-2 rounded-full border-red-700"
                    >
                        <p
                            class="text-base font-bold leading-normal text-center text-gray-900"
                        >
                            Cancel
                        </p>
                    </button>
                    <button
                        @click="confirmAcceptDisRequest1"
                        class="focus:outline-none inline-flex items-center justify-center w-52 px-3 py-1 bg-red-700 rounded-full"
                    >
                        <p
                            class="text-base font-bold leading-normal text-center text-white"
                        >
                            Confirm
                        </p>
                    </button>
                </div>
            </div>
        </div>
    </transition>
    <!--end-->

    <!--Decline User Request Button Modal-->
    <transition name="fadeSlide">
        <div
            v-if="declineRequest"
            class="z-50 fixed inset-0 flex justify-center items-center ssm:px-2 vs:px-2"
        >
            <div
                class="inline-flex flex-col bg-white shadow rounded-xl h-auto w-95 space-y-4 p-4 ssm:w-full vs:w-full"
            >
                <div class="flex justify-between items-center flex-row">
                    <button
                        class="invisible focus:outline-none text-sm font-bold leading-none text-right text-indigo-900"
                    >
                        Back</button
                    ><!--invisible, used only for auto margin header. If design need close button just delete the invisible class-->
                    <p
                        class="text-lg ssm:text-sm vs:text-base font-bold leading-normal text-center text-gray-900"
                    >
                        Decline Asta's Request
                    </p>
                    <button
                        @click="declineDisRequest1"
                        class="focus:outline-none text-sm font-bold leading-none text-right text-indigo-900"
                    >
                        Close
                    </button>
                </div>
                <hr class="w-full" />
                <div class="flex w-full">
                    <p
                        class="block items-start leading-normal text-base text-gray-900"
                    >
                        Are you sure you want to decline Asta's request? You can
                        not undo this.
                    </p>
                </div>
                <div class="justify-between flex flex-row space-x-2 w-full">
                    <button
                        @click="declineDisRequest1"
                        class="focus:outline-none inline-flex items-center justify-center w-52 px-3 py-1 border-2 rounded-full border-red-700"
                    >
                        <p
                            class="text-base font-bold leading-normal text-center text-gray-900"
                        >
                            Cancel
                        </p>
                    </button>
                    <button
                        @click="confirmDeclineDisRequest1"
                        class="focus:outline-none inline-flex items-center justify-center w-52 px-3 py-1 bg-red-700 rounded-full"
                    >
                        <p
                            class="text-base font-bold leading-normal text-center text-white"
                        >
                            Confirm
                        </p>
                    </button>
                </div>
            </div>
        </div>
    </transition>
    <!--end-->

    <!--Accept Offer Modal-->
    <div
        v-if="acceptOffer"
        class="z-50 fixed bg-black bg-opacity-25 inset-0 flex justify-center items-center ssm:px-2 vs:px-2"
    >
        <div
            class="inline-flex flex-col bg-white shadow rounded-xl h-auto w-96.5 space-y-4 p-4 ssm:w-full vs:w-full"
        >
            <div class="flex justify-between items-center flex-row">
                <button
                    class="invisible focus:outline-none text-sm font-bold leading-none text-right text-indigo-900"
                >
                    Back</button
                ><!--invisible, used only for auto margin header. If design need close button just delete the invisible class-->
                <p
                    class="text-lg ssm:text-sm vs:text-base font-bold leading-normal text-center text-gray-900"
                >
                    Accept Asta's {{ transaction }}
                </p>
                <button
                    @click="acceptDisOffer"
                    class="focus:outline-none text-sm font-bold leading-none text-right text-indigo-900"
                >
                    Close
                </button>
            </div>
            <hr class="w-full" />
            <div class="flex w-full">
                <p
                    class="block items-start leading-normal text-base text-gray-900"
                >
                    Are you sure you want to accept Asta's {{ transaction }}?
                    This would decline all other offers you received for this
                    post and will automatically update your post into
                    <span class="font-bold text-green-600 leading-normal"
                        >Order Taken</span
                    >.
                </p>
            </div>
            <div class="justify-between flex flex-row space-x-2 w-full">
                <button
                    @click="acceptDisOffer"
                    class="focus:outline-none inline-flex items-center justify-center w-52 px-3 py-1 border-2 rounded-full border-red-700"
                >
                    <p
                        class="text-base font-bold leading-normal text-center text-gray-900"
                    >
                        Cancel
                    </p>
                </button>
                <button
                    @click="confirmAcceptDisRequest2"
                    class="focus:outline-none inline-flex items-center justify-center w-52 px-3 py-1 bg-red-700 rounded-full"
                >
                    <p
                        class="text-base font-bold leading-normal text-center text-white"
                    >
                        Confirm
                    </p>
                </button>
            </div>
        </div>
    </div>
    <!--end-->

    <!--Decline Offer Modal-->
    <div
        v-if="declineOffer"
        class="z-50 fixed bg-black bg-opacity-25 inset-0 flex justify-center items-center ssm:px-2 vs:px-2"
    >
        <div
            class="inline-flex flex-col bg-white shadow rounded-xl h-auto w-95 space-y-4 p-4 ssm:w-full vs:w-full"
        >
            <div class="flex justify-between items-center flex-row">
                <button
                    class="invisible focus:outline-none text-sm font-bold leading-none text-right text-indigo-900"
                >
                    Back</button
                ><!--invisible, used only for auto margin header. If design need close button just delete the invisible class-->
                <p
                    class="text-lg ssm:text-sm vs:text-base font-bold leading-normal text-center text-gray-900"
                >
                    Decline Asta's {{ transaction }}
                </p>
                <button
                    @click="declineDisOffer"
                    class="focus:outline-none text-sm font-bold leading-none text-right text-indigo-900"
                >
                    Close
                </button>
            </div>
            <hr class="w-full" />
            <div class="flex w-full">
                <p
                    class="block items-start leading-normal text-base text-gray-900"
                >
                    Are you sure you want to decline Asta's {{ transaction }}?
                    You can not undo this.
                </p>
            </div>
            <div class="justify-between flex flex-row space-x-2 w-full">
                <button
                    @click="declineDisOffer"
                    class="focus:outline-none inline-flex items-center justify-center w-52 px-3 py-1 border-2 rounded-full border-red-700"
                >
                    <p
                        class="text-base font-bold leading-normal text-center text-gray-900"
                    >
                        Cancel
                    </p>
                </button>
                <button
                    @click="confirmDeclineDisRequest2"
                    class="focus:outline-none inline-flex items-center justify-center w-52 px-3 py-1 bg-red-700 rounded-full"
                >
                    <p
                        class="text-base font-bold leading-normal text-center text-white"
                    >
                        Confirm
                    </p>
                </button>
            </div>
        </div>
    </div>
    <!--end-->

    <!--Cancellation Modal-->
    <div
        v-if="cancel"
        class="z-50 fixed bg-black bg-opacity-25 inset-0 flex justify-center items-center ssm:px-2 vs:px-2"
    >
        <div
            class="inline-flex flex-col bg-white shadow rounded-xl h-auto w-95 space-y-4 p-4 ssm:w-full vs:w-full"
        >
            <div class="flex justify-between items-center flex-row">
                <button
                    class="invisible focus:outline-none text-sm font-bold leading-none text-right text-indigo-900"
                >
                    Back</button
                ><!--invisible, used only for auto margin header. If design need close button just delete the invisible class-->
                <p
                    class="text-lg ssm:text-sm vs:text-base font-bold leading-normal text-center text-gray-900"
                >
                    Cancel Asta's {{ transaction }}
                </p>
                <button
                    @click="cancel_transact"
                    class="focus:outline-none text-sm font-bold leading-none text-right text-indigo-900"
                >
                    Close
                </button>
            </div>
            <hr class="w-full" />
            <div class="flex w-full">
                <p
                    class="block items-start leading-normal text-base text-gray-900"
                >
                    Are you sure you want to cancel Asta's {{ transaction }}?
                    You can not undo this.
                </p>
            </div>
            <div class="justify-between flex flex-row space-x-2 w-full">
                <button
                    @click="cancel_transact"
                    class="focus:outline-none inline-flex items-center justify-center w-52 px-3 py-1 border-2 rounded-full border-red-700"
                >
                    <p
                        class="text-base font-bold leading-normal text-center text-gray-900"
                    >
                        Cancel
                    </p>
                </button>
                <button
                    @click="confirmCancellation"
                    class="focus:outline-none inline-flex items-center justify-center w-52 px-3 py-1 bg-red-700 rounded-full"
                >
                    <p
                        class="text-base font-bold leading-normal text-center text-white"
                    >
                        Confirm
                    </p>
                </button>
            </div>
        </div>
    </div>
    <!--end-->

    <!--Accept PopUp Notification-->
    <div
        class="z-100 fixed inset-x-0 bottom-2 flex justify-center items-center"
    >
        <div
            v-if="acceptReqNotiPop"
            class="acceptRequestNotiPop bg-gray-900 text-white px-4 py-2 rounded-xl w-95 h-auto"
            role="alert"
        >
            <div class="flex w-full flex-row justify-between items-center">
                <div class="flex flex-row w-full space-x-2">
                    <span
                        class="w-6 h-6 rounded-full material-icons text-white"
                    >
                        check_circle
                    </span>
                    <p class="text-base leading-normal text-white">
                        Successfully Accepted Asta's Request
                    </p>
                </div>
                <button
                    @click="closeAcceptRequestNotiPop"
                    class="focus:outline-none flex"
                >
                    <span
                        class="w-6 h-6 rounded-full material-icons text-white"
                    >
                        cancel
                    </span>
                </button>
            </div>
        </div>
    </div>
    <!--end-->

    <!--Decline PopUp Notification-->
    <div
        class="z-100 fixed inset-x-0 bottom-2 flex justify-center items-center"
    >
        <div
            v-if="declineReqNotiPop"
            class="declineRequestNotiPop bg-gray-900 text-white px-4 py-2 rounded-xl w-95 h-auto"
            role="alert"
        >
            <div class="flex w-full flex-row justify-between items-center">
                <div class="flex flex-row w-full space-x-2">
                    <span
                        class="w-6 h-6 rounded-full material-icons text-white"
                    >
                        check_circle
                    </span>
                    <p class="text-base leading-normal text-white">
                        Successfully Declined Asta's Request
                    </p>
                </div>
                <button
                    @click="closeDeclineRequestNotiPop"
                    class="focus:outline-none flex"
                >
                    <span
                        class="w-6 h-6 rounded-full material-icons text-white"
                    >
                        cancel
                    </span>
                </button>
            </div>
        </div>
    </div>
    <!--end-->

    <!--Cancel PopUp Notification-->
    <div
        class="z-100 fixed inset-x-0 bottom-2 flex justify-center items-center"
    >
        <div
            v-if="confirmCancel"
            class="declineRequestNotiPop bg-gray-900 text-white px-4 py-2 rounded-xl w-95 h-auto"
            role="alert"
        >
            <div class="flex w-full flex-row justify-between items-center">
                <div class="flex flex-row w-full space-x-2">
                    <span
                        class="w-6 h-6 rounded-full material-icons text-white"
                    >
                        check_circle
                    </span>
                    <p class="text-base leading-normal text-white">
                        {{ transaction }} cancelled!
                    </p>
                </div>
                <button
                    @click="confirmCancel = false"
                    class="focus:outline-none flex"
                >
                    <span
                        class="w-6 h-6 rounded-full material-icons text-white"
                    >
                        cancel
                    </span>
                </button>
            </div>
        </div>
    </div>
    <!--end-->

    <!----update status--->
    <div
        v-if="toggle_status"
        class="fixed bg-black z-100 h-max w-screen bg-opacity-75 overflow-y-auto items-center inset-0"
    >
        <div class="flex mt-4 w-full p-3 items-center justify-center py-20">
            <div
                class="bg-white ring-1 ring-gray-300 p-5 w-full rounded-xl 2xl:w-97 lg:w-97 xl:w-97 xl:mr-16 md:w-8/12 sm:w-10/12 shadow-2xl h-auto"
            >
                <div class="flex flex-row items-center justify-between p-3">
                    <p class="hidden lg:block 2xl:block xl:block"></p>
                    <p class="text-lg font-bold xl:ml-8 lg:ml-8 2xl:ml-8">
                        Update Transaction Status
                    </p>
                    <p
                        class="font-bold text-blue-700 cursor-pointer left-10"
                        @click="toggle_status = false"
                    >
                        Close
                    </p>
                </div>
                <hr />
                <div class=" ">
                    <div class="flex flex-col p-3 space-y-4">
                        <span class="flex items-center space-x-2"
                            ><input
                                type="radio"
                                name="status"
                                value="Completed"
                            /><span>Completed</span></span
                        >
                        <span class="flex items-center space-x-2"
                            ><input
                                type="radio"
                                name="status"
                                value="Comfirmed"
                            /><span>Confirmed</span></span
                        >
                        <span class="flex items-center space-x-2"
                            ><input
                                type="radio"
                                name="status"
                                value="In Transit"
                            /><span>In Transit</span></span
                        >
                        <span class="flex items-center space-x-2"
                            ><input
                                type="radio"
                                name="status"
                                value="Cancelled"
                            /><span>Cancelled</span></span
                        >
                    </div>
                </div>
                <div class="flex justify-between mt-4 items-center">
                    <button
                        @click="toggle_status = false"
                        class="bg-red-buttons text-white focus:outline-none w-full h-7 shadow-xl ring-1 ring-gray-300 rounded-2xl"
                    >
                        Update
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import $ from "jquery";
import Navbar from "./Navbar";
var file = "";
export default {
    components: {
        Navbar,
    },
    props: {
        //message: String
    },
    computed: {
        computedShopItemList() {
            return this.limit_by
                ? this.filter_itemList.slice(0, this.limit_by)
                : this.filter_itemList;
        },
        isFew: ({ filter_itemList }) => filter_itemList.length < 5,
        computedRequestReceived() {
            return this.limitRequestDisplay
                ? this.RequsetReceived.slice(0, this.limitRequestDisplay)
                : this.RequsetReceived;
        },
    },
    data() {
        return {
            //buttons
            toggle: false,
            toggleInbox: true,
            toggleChat: false,
            toggleVerti: false,
            searchMessageInactive: true,
            showSearchResults: false,
            attachment: false,
            ifHide: true,
            toggle1: true,
            toggle2: false,
            toggle3: false,
            toggle4: false,
            toggle5: false,
            toggle6: false,
            toggle7: false,
            attach: "add",
            active: "toggle1",

            countItems: 8,
            viewDetails: false,
            acceptRequest: false,
            declineRequest: false,
            acceptReqNotiPop: false,
            declineReqNotiPop: false,
            acceptOffer: false,
            declineOffer: false,

            toggle_status: false,
            transaction: "",
            cancel: false,
            confirmCancel: false,

            request_info: {
                delivery_area: "Banquerohan Legazpi City",
                shopping_place: "SM City Legazpi",
                schedule: "Tomorrow at 5:00 PM",
                payment_method: "Payment First",
                comment:
                    "Hello sis! Pwede pasabuy me? Wes akes time para gumora sa market huhuhu accept my request juseyo!! labyu hehehe",
            },
            filter_itemList: [
                {
                    item: "flour",
                    amount: "1 kg",
                    brand: "Any brand",
                    unit: "2 units",
                },
                {
                    item: "flour",
                    amount: "1 kg",
                    brand: "Any brand",
                    unit: "2 units",
                },
                {
                    item: "flour",
                    amount: "1 kg",
                    brand: "Any brand",
                    unit: "2 units",
                },
                {
                    item: "flour",
                    amount: "1 kg",
                    brand: "Any brand",
                    unit: "2 units",
                },
                {
                    item: "flour",
                    amount: "1 kg",
                    brand: "Any brand",
                    unit: "2 units",
                },
                {
                    item: "flour",
                    amount: "1 kg",
                    brand: "Any brand",
                    unit: "2 units",
                },
                {
                    item: "flour",
                    amount: "1 kg",
                    brand: "Any brand",
                    unit: "2 units",
                },
                {
                    item: "flour",
                    amount: "1 kg",
                    brand: "Any brand",
                    unit: "2 units",
                },
            ],

            default_limit: 4,
            showListStatus: "See More",
            showLessStatus: "See Less",
            limit_by: 4,
            //inbox
            inbox: [
                {
                    name: "Mark Aral",
                    message: "No problem. Thanks as well for the handsome pay!",
                    time: "21 mins",
                },
                {
                    name: "Gwen Lopez",
                    message:
                        "No problem. Thanks as well for the handsome pay! No problem. Thanks as well for the handsome pay!",
                    time: "21 mins",
                },
            ],
            //chat
            activeName: "Mark Aral",
            chatIncoming: [
                {
                    received:
                        "Yeah, sure! No problem. I am already on my way to SM City Legazpi.",
                    timeReceived: "1:26 PM    |    Today",
                },
                {
                    received:
                        "Sorry, it took me a while. I had to shop for three orders. Anyway, I am already in my car. I will deliver these two orders first here in Legazpi.",
                    timeReceived: "2:40 PM    |    Today",
                },
                {
                    received: "I am two mins away from your house. ",
                    timeReceived: "3:12 PM    |    Today",
                },
                {
                    received:
                        "No problem. Thanks as well for the handsome pay!",
                    timeReceived: "3:39 PM    |    Today",
                },
            ],
            chatOutgoing: [
                {
                    sent: "Do you think you can do it in time? I need it before 4 pm so I hope you can deliver it in time.",
                    timeSent: "1:24 PM    |    Today",
                },
                {
                    sent: "Thank you so much! Let me know when you are on your way.",
                    timeSent: "1:31 PM    |    Today",
                },
                {
                    sent: "No problem, chat me when you are near my house already",
                    timeSent: "2:45 PM    |    Today",
                },
                { sent: "Thanks for help", timeSent: "3:36  | Today" },
            ],
            //sent a request
            activity: "You sent a request to to",
            recipient: "Mark Aral",
            sender: "Monica Rambeau",
            postNum: "#2021352",
            postNum2: "#130317",
            placeFrom: "Banquerohan, Legazpi City",
            destination: "SM City ",
            timeAlloted: "Tomorrow, 5 PM",
            paymentMethod: "Payment First via GCash transfer",
            //shoppingList
            shoppingList: [
                { items: "Baking Soda" },
                { items: "Choco Syrup" },
                { items: "cocoa powder" },
                { items: "flour 1 kg" },
                { items: "brown sugar" },
                { items: "cocoa powder" },
            ],
            shoppingListSize: 8,
        };
    },
    methods: {
        sendbtn() {
            const fileInputBtn = document.getElementById("fileInput");
            var printtext = document.getElementById("chatmsg-DESKTOP");
            var printtext2 = document.getElementById("chatmsg-MOBILE");
            var copytext = document.getElementById("typemsg-DESKTOP");
            var copytext2 = document.getElementById("typemsg-MOBILE");
            var copiedtext = copytext.value;
            var copiedtext2 = copytext2.value;

            if (copiedtext !== "") {
                var printnow =
                    '<div class="p-2 flex justify-end ">' +
                    '<div class="ml-32 pt-2 pl-4 pb-3 pr-4 bg-gray-100 text-sm rounded-lg">' +
                    copiedtext +
                    '<span class="time_date text-gray-500 pl-1" style="font-size: 10.5px;" >' +
                    "<br>" +
                    "3:45 PM" +
                    " | " +
                    "Today" +
                    "</span>" +
                    "</div> ";
                printtext.insertAdjacentHTML("beforeend", printnow);
                document.getElementById("typemsg-DESKTOP").value = "";
                printtext2.insertAdjacentHTML("beforeend", printnow2);
                document.getElementById("typemsg-MOBILE").value = "";
            }
            if (copiedtext2 !== "") {
                var printnow2 =
                    '<div class="p-2 flex justify-end ">' +
                    '<div class="ml-32 pt-2 pl-4 pb-3 pr-4 bg-gray-100 text-sm rounded-lg">' +
                    copiedtext +
                    '<span class="time_date text-gray-500 pl-1" style="font-size: 10.5px;" >' +
                    "<br>" +
                    "3:45 PM" +
                    " | " +
                    "Today" +
                    "</span>" +
                    "</div> ";
                printtext2.insertAdjacentHTML("beforeend", printnow2);
                document.getElementById("typemsg-MOBILE").value = "";
                printtext.insertAdjacentHTML("beforeend", printnow);
                document.getElementById("typemsg-DESKTOP").value = "";
            }
            if (fileInputBtn.value) {
                //alert(file);
                var printFile =
                    '<div class="p-2 flex justify-end ">' +
                    '<div class="ml-32 pt-2 pl-4 pb-3 pr-4 bg-gray-100 text-sm rounded-lg">' +
                    file +
                    "</div> ";
                printtext.insertAdjacentHTML("beforeend", printFile);
                printtext2.insertAdjacentHTML("beforeend", printFile);
                document.getElementById("typemsg-MOBILE").value = "";
                document.getElementById("typemsg-DESKTOP").value = "";
                this.attachment = !this.attachment;
                if (this.attachment == true) {
                    document.getElementById("attach").innerHTML = "close";
                } else if (this.attachment == false) {
                    document.getElementById("attach").innerHTML = "add";
                }
            } //end if
        }, //end sendbtn
        searchBtn() {
            this.showSearchResults = !this.showSearchResults;
            this.searchMessageInactive = !this.searchMessageInactive;
            document.getElementByID("search").value = "Mark";
        },
        alert() {
            alert("called");
        },
        closeSearchResults() {
            if (this.searchMessageInactive == false) {
                this.searchMessageInactive = !this.searchMessageInactive;
                this.showSearchResults = !this.showSearchResults;
            }
        },
        searchBackBtn() {
            this.showSearchResults = !this.showSearchResults;
            this.searchMessageInactive = !this.searchMessageInactive;
        },
        attachbtn() {
            this.attachment = !this.attachment;
            if (this.attachment == true) {
                document.getElementById("attach").innerHTML = "close";
                document.getElementById("attach2").innerHTML = "close";
            } else if (this.attachment == false) {
                document.getElementById("attach").innerHTML = "add";
                document.getElementById("attach2").innerHTML = "add";
            }
        },
        navigate() {
            this.toggleInbox = !this.toggleInbox;
            this.toggleChat = !this.toggleChat;
            var b = document.getElementById("mark");
            var bText = b.textContent;
            var bLen = bText.length;
            var res = bText.substring(0, bLen - 13);
            document.getElementById("active").innerHTML = res;
        },
        active_convo(el) {
            this.toggleInbox = !this.toggleInbox;
            this.toggleChat = !this.toggleChat;
            //console.log(el);
            this.activeName = el;
        },
        backChat() {
            this.toggleInbox = !this.toggleInbox;
            this.toggleChat = !this.toggleChat;
        },
        threedots() {
            this.toggle = !this.toggle;
        }, //end threedots
        vertiDots() {
            this.toggleVerti = !this.toggleVerti;
        }, //end funtion vertiDots
        attachPhoto() {
            const fileInputBtn = document.getElementById("photoInput");
            const fileholder = document.getElementById("photo");
            fileInputBtn.click();
            fileInputBtn.addEventListener("change", function () {
                if (fileInputBtn.value) {
                    fileholder.innerHTML = fileInputBtn.value;
                } else {
                    fileholder.innerhtml = "";
                }
            });
        },
        attachFile() {
            const fileInputBtn = document.getElementById("fileInput");
            //const fileholder = document.getElementById('file');
            fileInputBtn.click();

            $(document).ready(function () {
                $('input[type="file"]').change(function (e) {
                    var geekss = e.target.files[0].name;
                    file = geekss;
                    $("label").text(geekss);
                    //alert(this.fileName);
                });
            });
        },
        hideVertiOptions() {
            this.ifHide = false;
        },
        showVertiOptions() {
            this.ifHide = true;
            this.toggle = false;
            this.toggleVerti = false;
        },
        active_transact(e) {
            if (this.active === "toggle1") this.toggle1 = false;
            else if (this.active === "toggle2") this.toggle2 = false;
            else if (this.active === "toggle3") this.toggle3 = false;
            else if (this.active === "toggle4") this.toggle4 = false;
            else if (this.active === "toggle5") this.toggle5 = false;
            else if (this.active === "toggle6") this.toggle6 = false;

            switch (e) {
                case "toggle1": {
                    if (this.toggle1 !== true) {
                        this.toggle1 = !this.toggle1;
                        this.active = "toggle1";
                    }
                    break;
                }
                case "toggle2": {
                    if (this.toggle2 !== true) {
                        this.toggle2 = !this.toggle2;
                        this.active = "toggle2";
                    }
                    break;
                }
                case "toggle3": {
                    if (this.toggle3 !== true) {
                        this.toggle3 = !this.toggle3;
                        this.active = "toggle3";
                    }
                    break;
                }
                case "toggle4": {
                    if (this.toggle4 !== true) {
                        this.toggle4 = !this.toggle4;
                        this.active = "toggle4";
                    }
                    break;
                }
                case "toggle5": {
                    if (this.toggle5 !== true) {
                        this.toggle5 = !this.toggle5;
                        this.active = "toggle5";
                    }
                    break;
                }
                case "toggle6": {
                    if (this.toggle6 !== true) {
                        this.toggle6 = !this.toggle;
                        this.active = "toggle6";
                    }
                    break;
                }
                default:
                    this.toggle1 = true;
            } //end switch

            this.toggleVerti = false;
        },
        toggleViewDetails() {
            this.viewDetails = !this.viewDetails;
        },

        acceptDisRequest() {
            $(".hideMe1").fadeOut();
            this.acceptRequest = !this.acceptRequest;
        },

        declineDisRequest() {
            $(".hideMe1").fadeOut();
            this.declineRequest = !this.declineRequest;
        },

        acceptDisRequest1() {
            this.acceptRequest = !this.acceptRequest;
            $(".hideMe1").fadeIn();
        },

        confirmAcceptDisRequest1() {
            this.acceptRequest = !this.acceptRequest;
            this.viewDetails = !this.viewDetails;
            setTimeout(() => {
                $(".acceptRequestNotiPop").fadeIn(),
                    (this.acceptReqNotiPop = true);
            }, 500);

            setTimeout(function () {
                this.acceptReqNotiPop = false;
                $(".acceptRequestNotiPop").fadeOut();
            }, 4000);
        },

        confirmAcceptDisRequest2() {
            this.acceptOffer = !this.acceptOffer;
            setTimeout(() => {
                $(".acceptOfferNotiPop").fadeIn(),
                    (this.acceptReqNotiPop = true);
            }, 500);

            setTimeout(function () {
                this.acceptOffer = false;
                $(".acceptOfferNotiPop").fadeOut();
            }, 4000);
        },

        closeAcceptRequestNotiPop() {
            this.acceptReqNotiPop = false;
            $(".acceptRequestNotiPop").fadeOut();
        },
        confirmDeclineDisRequest1() {
            this.declineRequest = !this.declineRequest;
            this.viewDetails = !this.viewDetails;
            setTimeout(() => {
                $(".declineRequestNotiPop").fadeIn(),
                    (this.declineReqNotiPop = true);
            }, 500);

            setTimeout(function () {
                this.declineReqNotiPop = false;
                $(".declineRequestNotiPop").fadeOut();
            }, 4000);
        },

        confirmDeclineDisRequest2() {
            this.declineOffer = !this.declineOffer;
            setTimeout(() => {
                $(".declineOfferNotiPop").fadeIn(),
                    (this.declineReqNotiPop = true);
            }, 500);

            setTimeout(function () {
                this.declineReqNotiPop = false;
                $(".declineOfferNotiPop").fadeOut();
            }, 4000);
        },

        closeDeclineRequestNotiPop() {
            this.declineReqNotiPop = false;
            $(".declineRequestNotiPop").fadeOut();
        },

        declineDisRequest1() {
            this.declineRequest = !this.declineRequest;
            $(".hideMe1").fadeIn();
        },

        showMoreshowLess() {
            this.limit_by = null;
            if (this.showListStatus != this.showLessStatus) {
                this.showListStatus = this.showLessStatus;
            } else {
                this.showListStatus = "See More";
                this.limit_by = this.default_limit;
            }
        },
        acceptDisOffer(e) {
            this.acceptOffer = !this.acceptOffer;
            this.transaction = e;
        },

        declineDisOffer(e) {
            this.declineOffer = !this.declineOffer;
            this.transaction = e;
        },

        cancel_transact(e) {
            this.cancel = !this.cancel;
            this.transaction = e;
        },

        confirmCancellation() {
            this.confirmCancel = !this.confirmCancel;
            this.cancel = !this.cancel;
        },
    }, //end methods
}; //end export default
$(document).mouseup(function (e) {
    //desktop
    var delBtn = $("#delBtn");
    var vertiOPTIONS = $("#vertiOPTIONS");
    // If the target of the click isn't the container
    if (!delBtn.is(e.target) && delBtn.has(e.target).length === 0) {
        delBtn.hide();
    }
    if (!vertiOPTIONS.is(e.target) && vertiOPTIONS.has(e.target).length === 0) {
        vertiOPTIONS.hide();
    }
    //mobile
    var delBtn_MOBILE = $("#delBtn-MOBILE");
    var vertiOPTIONS_MOBILE = $("#vertiOPTIONS-MOBILE");
    // If the target of the click isn't the container
    if (
        !delBtn_MOBILE.is(e.target) &&
        delBtn_MOBILE.has(e.target).length === 0
    ) {
        delBtn_MOBILE.hide();
    }
    if (
        !vertiOPTIONS_MOBILE.is(e.target) &&
        vertiOPTIONS_MOBILE.has(e.target).length === 0
    ) {
        vertiOPTIONS_MOBILE.hide();
    }
});
</script>

<style>
.hide {
    display: none;
}
#journal-scroll::-webkit-scrollbar {
    width: 3px;
    cursor: pointer;
}
#journal-scroll::-webkit-scrollbar-track {
    background-color: rgba(229, 231, 235, var(--bg-opacity));
    cursor: pointer;
}
#scrollInbox::-webkit-scrollbar-thumb {
    cursor: pointer;
    background-color: rgba(185, 28, 28);
}
#scrollInbox::-webkit-scrollbar {
    width: 2px;
    cursor: pointer;
}
#scrollInbox::-webkit-scrollbar-track {
    background-color: rgba(219, 216, 216, var(--bg-opacity));
    cursor: pointer;
}
#scrollInbox::-webkit-scrollbar-thumb {
    cursor: pointer;
    background-color: rgb(219, 216, 216);
}
/*minimized desktop version and mobile version
screen sizes lesser than 639px*/
.desktopVersion {
    display: none;
}
.mobileVersion {
    display: inline;
}
#backNavigator {
    display: inline;
}
#msgheader {
    display: none;
}
#vertiOPTIONS-MOBILE {
    box-shadow: 1px 1px 1px 1px #888888;
}
/*for screen sizes 639px++*/
@media only screen and (min-width: 639px) {
    .desktopVersion {
        display: inline;
    }
    .mobileVersion {
        display: none;
    }
    #backNavigator {
        display: none;
    }
    #msgheader {
        display: flex;
    }
}
#iCheck {
    font-size: 16px;
    color: rgb(22, 22, 141);
}
#iMessage {
    font-size: 24px;
    color: rgb(22, 22, 141);
}
.material-icons {
    font-family: "Material Icons";
    font-weight: normal;
    font-style: normal;
    line-height: 1;
    text-transform: none;
    letter-spacing: normal;
    word-wrap: normal;
    white-space: nowrap;
    direction: ltr;
    /* Support for all WebKit browsers. */
    -webkit-font-smoothing: antialiased;
    /* Support for Safari and Chrome. */
    text-rendering: optimizeLegibility;
    /* Support for Firefox. */
    -moz-osx-font-smoothing: grayscale;
    /* Support for IE. */
    font-feature-settings: "liga";
}

.fadeSlide-enter-from {
    transform: translateX(100%);
    transform: translateX(150px);
    opacity: 0;
}
.fadeSlide-enter-to {
    transform: translateX(0);
    opacity: 1;
}
.fadeSlide-enter-active {
    transition: all 0.3s ease-in-out;
}

.fadeSlide-leave-from {
    transform: translateX(0);
    opacity: 1;
}
.fadeSlide-leave-to {
    transform: translateX(100%);
    transform: translateX(150px);
    opacity: 0;
}
.fadeSlide-leave-active {
    transition: all 0.3s ease-in-out;
}
</style>
