/* angular.module('ExampleApp', ['g1b.scroll-events', 'g1b.datetime-inputs', 'g1b.datetime-range']).*/

controller('MainCtrl', function ($scope) {

  // Datetime inputs initial variable
  $scope.now = moment();

  // Datetime range start/end vars
  $scope.start = moment();
  $scope.end = moment().add(1, 'days').add(1, 'hours');

  // Datetime range presets
  $scope.presets = [
    {
      'name': 'This Week',
      'start': moment().startOf('week').startOf('day'),
      'end': moment().endOf('week').endOf('day'),
    }, {
      'name': 'This Month',
      'start': moment().startOf('month').startOf('day'),
      'end': moment().endOf('month').endOf('day'),
    }, {
      'name': 'This Year',
      'start': moment().startOf('year').startOf('day'),
      'end': moment().endOf('year').endOf('day'),
    }
  ];

  // Datetime input on change callback
  $scope.print = function (datetime) {
  };

  // Datetime range on change callback
  $scope.changed = function () {
    console.log('changed start or end datetime objects');
  };

  // Datetime
  $scope.changedStart = function () {
    console.log('changed start datetime object');
  };
  $scope.changedEnd = function () {
    console.log('changed end datetime object');
  };
  $scope.closed = function () {
    console.log('edit popover closed');
  };
});