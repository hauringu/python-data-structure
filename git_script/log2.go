package log

import (
	"encoding/json"
	"fmt"

	"git.code.oa.com/trpc-go/trpc-go/log"
)

// ToStringFormat ..
func ToStringFormat(v interface{}) string {
	bData, err := json.MarshalIndent(v, "", "\t")
	if err != nil {
		return "MarshalIndent err"
	}

	return string(bData)
}

// ToString ...
func ToString(v interface{}) string {
	bData, err := json.Marshal(v)
	if err != nil {
		return "@error@"
	}

	return string(bData)
}

// Sprintf ...
func Sprintf(str string, a ...interface{}) string {
	bstr := []rune(str)
	pos := 0
	for i := 0; i < len(bstr)-1; i++ {
		if bstr[i] != '%' {
			continue
		}
		i++
		if bstr[i] == 'j' {
			a[pos] = ToString(a[pos])
			bstr[i] = 's'
		} else if bstr[i] == 'J' {
			a[pos] = ToStringFormat(a[pos])
			bstr[i] = 's'
		}
		if bstr[i] != '%' {
			pos++
		}
	}
	return fmt.Sprintf(string(bstr), a...)
}

// Debugf 支持 "%j" 和 "%J" 来打印json格式日志.
func Debugf(str string, args ...interface{}) {
	if log.GetLevel("0") > log.LevelDebug {
		return
	}
	log.Debug(Sprintf(str, args...))
}

// Debug ...
func Debug(args ...interface{}) {
	log.Debug(args...)
}

// Infof 支持 "%j" 和 "%J" 来打印json格式日志
func Infof(str string, args ...interface{}) {
	if log.GetLevel("0") > log.LevelInfo {
		return
	}
	log.Info(Sprintf(str, args...))
}

// Info ...
func Info(args ...interface{}) {
	log.Info(args...)
}

// Warnf 支持 "%j" 和 "%J" 来打印json格式日志
func Warnf(str string, args ...interface{}) {
	if log.GetLevel("0") > log.LevelWarn {
		return
	}
	log.Warn(Sprintf(str, args...))
}

// Warn ...
func Warn(args ...interface{}) {
	log.Warn(args...)
}

// Errorf 支持 "%j" 和 "%J" 来打印json格式日志
func Errorf(str string, args ...interface{}) {
	if log.GetLevel("0") > log.LevelError {
		return
	}
	log.Error(Sprintf(str, args...))
}

// Error ...
func Error(args ...interface{}) {
	log.Error(args...)
}

// Fatalf 支持 "%j" 和 "%J" 来打印json格式日志
func Fatalf(str string, args ...interface{}) {
	if log.GetLevel("0") > log.LevelFatal {
		return
	}
	log.Fatal(Sprintf(str, args...))
}

// Fatal ...
func Fatal(args ...interface{}) {
	log.Fatal(args...)
}
