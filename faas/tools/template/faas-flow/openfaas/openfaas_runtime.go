package openfaas

import (
	"fmt"
	"github.com/faasflow/runtime"
	sdk "github.com/faasflow/sdk"
	"github.com/faasflow/sdk/executor"
	"handler/eventhandler"
)

type OpenFaasRuntime struct {
	stateStore   sdk.StateStore
	dataStore    sdk.DataStore
	eventHandler sdk.EventHandler
}

func (ofRuntime *OpenFaasRuntime) Init() error {
	var err error
	ofRuntime.stateStore, err = initStateStore()
	if err != nil {
		return fmt.Errorf("Failed to initialize the StateStore, %v", err)
	}

	ofRuntime.dataStore, err = initDataStore()
	if err != nil {
		return fmt.Errorf("Failed to initialize the StateStore, %v", err)
	}

	ofRuntime.eventHandler = &eventhandler.FaasEventHandler{}

	return nil
}

func (ofRuntime *OpenFaasRuntime) CreateExecutor(request *runtime.Request) (executor.Executor, error) {
	ex := &OpenFaasExecutor{StateStore: ofRuntime.stateStore, DataStore: ofRuntime.dataStore, EventHandler: ofRuntime.eventHandler}
	error := ex.Init(request)
	return ex, error
}
