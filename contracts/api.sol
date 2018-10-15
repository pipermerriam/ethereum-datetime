contract DateTimeAPI {
        /*
         *  Abstract contract for interfacing with the DateTime contract.
         *
         */
        function isLeapYear(uint16 year) constant returns (bool);
        function getYear(uint timestamp) constant returns (uint16);
        function getMonth(uint timestamp) constant returns (uint8);
        function getDay(uint timestamp) constant returns (uint8);
        function getHour(uint timestamp) constant returns (uint8);
        function getMinute(uint timestamp) constant returns (uint8);
        function getSecond(uint timestamp) constant returns (uint8);
        function getWeekday(uint timestamp) constant returns (uint8);
        function toTimestamp(uint16 year, uint8 month, uint8 day) constant returns (uint timestamp);
        function toTimestamp(uint16 year, uint8 month, uint8 day, uint8 hour) constant returns (uint timestamp);
        function toTimestamp(uint16 year, uint8 month, uint8 day, uint8 hour, uint8 minute) constant returns (uint timestamp);
        function toTimestamp(uint16 year, uint8 month, uint8 day, uint8 hour, uint8 minute, uint8 second) constant returns (uint timestamp);
        function addYears(uint timestamp, uint16 addingYears) public pure returns (uint);
        function addMonths(uint timestamp, uint16 addingMonths) public pure returns (uint);
        function addDays(uint timestamp, uint16 addingDays) public pure returns (uint);
        function subYears(uint timestamp, uint16 subtractingYears) public pure returns (uint);
        function subMonths(uint timestamp, uint16 subtractingMonths) public pure returns (uint);
        function subDays(uint timestamp, uint16 subtractingDays) public pure returns (uint);
}

